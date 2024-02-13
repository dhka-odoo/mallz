from odoo import fields,models

class shop(models.Model):
    _name = "mall.shop"
    _description = "shop in the mall"

    name = fields.Char('Shop name',required=True)
    shop_num = fields.Integer('Shop no.')
    tenant_id = fields.Many2one('mall.tenant',string="Tenant")
    description = fields.Text('Description')
    floor_num = fields.Integer('Floor no.')
    shop_area = fields.Float('Shop Area (sqm)')
    shop_rent = fields.Float('Shop Rent')
    mall_name_id = fields.Many2one('malls',string="Mall name")
    state = fields.Selection(
        string='Status',
        selection=[('New','New'),('Offer_Received','Offer Received'),('Offer_Accepted','Offer Accepted'),('Sold','Sold'),('Canceled','Canceled')],
        default='New'
    )
    offer_ids = fields.One2many("mall.shop.offer","shop_id", string="Offers")
