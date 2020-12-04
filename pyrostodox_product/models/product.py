# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    link = fields.Char(string="CLEART")
    oem = fields.Char(string="OEM", help="Reference of the Producer")
    upc = fields.Char(string="UPC", help="EAN US")
    manufacturer_id = fields.Many2one('res.partner', string="Manufacturer")  # MANUFACTURER: missing in the list
    is_available = fields.Boolean(string="Is Available")  # DISPO: in the list it's not a boolean!
    date_available = fields.Date(string="Date of Availability")  # DATE DISPO: missing in the list
    product_notes = fields.Text()  # RQPRODUIT: missing in the list
    public_price = fields.Float(string="Retail USD", help="Public Sales Price in USD")  # TARIF PUB
    public_price_currency_id = fields.Many2one('res.currency', default=lambda self: self.env['res.currency'].search([('name', 'like', 'usd')], limit=1))
    public_price_dif1 = fields.Float(string="Dealer Price EUR", help="First different Public Sales Price")  # TARIF 1
    public_price_dif1_currency_id = fields.Many2one('res.currency', default=lambda self: self.env['res.currency'].search([('name', 'like', 'eur')], limit=1))
    public_price_dif2 = fields.Float(string="Dealer Price EUR / Dropshipment", help="Second different Public Sales Price")  # TARIF 2
    public_price_dif2_currency_id = fields.Many2one('res.currency', default=lambda self: self.env['res.currency'].search([('name', 'like', 'eur')], limit=1))
    public_price_dif3 = fields.Float(string="Tarif 3", help="Third different Public Sales Price")  # TARIF 3: missing in the list
    public_price_dif3_currency_id = fields.Many2one('res.currency', default=lambda self: self.env['res.currency'].search([('name', 'like', 'eur')], limit=1))
    public_price_dif4 = fields.Float(string="Tarif 4", help="Forth different Public Sales Price")  # TARIF 4: missing in the list
    public_price_dif4_currency_id = fields.Many2one('res.currency', default=lambda self: self.env['res.currency'].search([('name', 'like', 'eur')], limit=1))
    no_tax_price = fields.Float(string="Retail EUR", help="Sales Price without Taxes in EUR")  # TARIF HT
    no_tax_price_currency_id = fields.Many2one('res.currency', default=lambda self: self.env['res.currency'].search([('name', 'like', 'eur')], limit=1))
    page = fields.Char(string="Catalogue Page")  # PAGE: in the list not Integer (e.g.; XXXX), is it alright?
    origin = fields.Many2one('res.country', string="Country of Production")
    weight = fields.Float(string="Weight")
    weight_unit = fields.Selection([('kg', 'kg'), ('lb', 'lb')])
    long_description = fields.Text()  # LONGDESCRIPTION: missing in the list, can be used as description, description_sale, etc?
    fam_web = fields.Text(string='WEB Family')  # TO BE DISCUSSED
    compatibility = fields.Text()  # can be also Char of HTML
    list_price = fields.Float(string="Dealer Price USD")

