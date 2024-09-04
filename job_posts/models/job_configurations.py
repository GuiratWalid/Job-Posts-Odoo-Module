from odoo import models, fields, api
from ..tools.webdriver import WebDriver

SCRAPING_STATE = [
    ('draft', 'Draft'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected')
]


class Posts(models.Model):
    _name = "job.configurations"
    _description = "Job configurations: scrapping and creating job posts."

    name = fields.Char(
        string="Reference",
        readonly=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('job.configurations')
    )
    targeted_position = fields.Char(
        string="Targeted Position",
        required=True,
    )
    state = fields.Selection(
        selection=SCRAPING_STATE,
        default="draft"
    )
    number_recovered_job_posts = fields.Integer(
        string="Number of Recovered Jobs",
        readonly=True,
        compute="_compute_number_recovered_job_posts",
        store=True
    )
    recovered_job_post_ids = fields.One2many(
        comodel_name="job.posts",
        inverse_name="source_id",
        string="Recovered Job Posts"
    )

    @api.depends("recovered_job_post_ids")
    def _compute_number_recovered_job_posts(self):
        """ Compute number of recovered job posts. """
        for record in self:
            if record.recovered_job_post_ids:
                record.number_recovered_job_posts = len(record.recovered_job_post_ids)
            else:
                record.number_recovered_job_posts = 0

    # Scraping posts method
    def scraping_posts(self):
        """ Scrap job posts from the TanitJob. """

        for record in self:
            if record.state == 'draft':
                TANITJOB_URL = f"https://www.tanitjobs.com/jobs/?listing_type%5Bequal%5D=Job&searchId=1725446388.784&action=search&keywords%5Ball_words%5D={record.targeted_position}&GooglePlace%5Blocation%5D%5Bvalue%5D=&GooglePlace%5Blocation%5D%5Bradius%5D=50"
                try:
                    """ Bypass 'Please Verify You Are a Human' using Selenium """

                    # Initialize the ChromeDriver
                    webDriver = WebDriver()
                    # webDriver("/home/walid/.cache/selenium/chromedriver/linux64/128.0.6613.119/chromedriver") # I use a local chromedriver

                    # Open a website
                    webDriver.open_website(TANITJOB_URL)

                    # Get elements
                    articles = webDriver.find_elements_by_class_name(
                        "media well listing-item listing-item__jobs listing-item__featured")

                    # Treat elements and create job posts
                    for article in articles:

                        # Get Job Post Attributes
                        tanit_job_id = article.get_attribute('id')
                        name = webDriver.find_element_by_tag_name_in_bloc(article, "a").text
                        link = webDriver.find_element_by_tag_name_in_bloc(article, "a").get_attribute('href')
                        publisher = webDriver.find_element_by_class_name_in_bloc(article, "listing-item__info--item listing-item__info--item-company").text
                        description = webDriver.find_element_by_class_name_in_bloc(article, "listing-item__desc hidden-sm hidden-xs").text
                        publication_date = webDriver.find_element_by_class_name_in_bloc(article, "listing-item__date").text
                        source_id = record.id

                        # Add only new posts
                        post_exists = self.env['job.posts'].search([('tanit_job_id', '=', tanit_job_id)])
                        if not post_exists:
                            self.env['job.posts'].create({
                                'tanit_job_id': tanit_job_id,
                                'name': name,
                                'link': link,
                                'publisher': publisher,
                                'description': description,
                                'publication_date': publication_date,
                                'source_id': source_id
                            })

                    # Quit the driver
                    webDriver.quit_driver()

                    # Set configuration's state to accepted
                    record.state = "accepted"
                except Exception:

                    # Set configuration's state to rejected
                    record.state = "rejected"



                    """ 
                        Cette version à améliorer pour prendre en considèration la pagination.
                        Pour le faire, nous pouvons créer un boucle "while" qui incrémente
                        le nombre de page (au niveau de l'URL) et répéter le même traitement 
                        jusqu'à trouver une page vide.
                     """
