# **Job Posts Odoo Module**

## **Overview**

The **Job Posts** module is an Odoo ERP extension designed to automate the process of retrieving job postings from [Tanitjob](https://www.tanitjobs.com/) using web scraping techniques. The module facilitates the management of these job posts within the Odoo platform, allowing users to efficiently track and process job opportunities.

## **Features**

- **Web Scraping**: Automatically fetches job postings from Tanitjob.
- **Job Management**: Stores and manages job postings within Odoo.
- **Automation**: Bypass CAPTCHA challenges using Selenium.
- **Search and Filter**: Ability to search for job posts by targeted position.
- **State Management**: Tracks the state of each job post scraping operation (Draft, Accepted, Rejected).
- **Database Integration**: Seamlessly integrates with the Odoo database to store and manage job posts.

## **Installation**

1. Clone this repository into your Odoo addons directory:
   **git clone https://github.com/GuiratWalid**
2. Update the Odoo module list:
   **./odoo-bin -u all**
3. Install the Job Posts module from the Odoo Apps menu.

## **Usage**

1. Navigate to the **Job Posts** module in your Odoo instance.
2. Create a new job configuration by specifying the targeted position.
3. Click on "Scrap" button to start the process. The module will retrieve job postings from **Tanitjob** based on searching keywords.
4. Review and manage the fetched job posts within the module.

## **Dependencies**

- **Odoo**: Version 14 or later.
- **Selenium**: For web scraping.

## **Contributing**

Feel free to fork this repository, make improvements, and submit pull requests.

## **Contact**

For any inquiries, please reach out to **[GuiratWalid](https://github.com/GuiratWalid)**.
