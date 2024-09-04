from odoo import models, fields


class Posts(models.Model):
    _name = "job.posts"
    _description = "Posts management"

    id = fields.Integer()
    name = fields.Char(
        string="Name",
        required=True
    )
    link = fields.Char(
        string="Link"
    )
    publisher = fields.Char(
        string="Publisher"
    )
    description = fields.Text(
        string="Description"
    )
    publication_date = fields.Date(
        string="Publication Date",
        default=fields.Date.today()
    )
    source_id = fields.Many2one(
        comodel_name="job.configurations",
        string="Source",
        readonly=True
    )
    assigned_user_id = fields.Many2one(
        comodel_name="res.partner",
        string="Assigned User"
    )
