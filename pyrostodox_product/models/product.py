# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    link = fields.Char()  # CLEART: not sure about the field type
    oem = fields.Char(string="OEM", help="Reference of the Producer")
    upc = fields.Char(string="UPC", help="EAN US")
    manufacturer_id = fields.Many2one('res.partner', string="Manufacturer")  # MANUFACTURER: missing in the list
    is_available = fields.Boolean(string="Is Available")  # DISPO: in the list it's not a boolean!
    date_available = fields.Date(string="Date of Availability")  # DATE DISPO: missing in the list
    product_notes = fields.Text()  # RQPRODUIT: missing in the list
    public_price = fields.Float(string="Public Price", help="Public Sales Price")  # TARIF PUB
    public_price_dif1 = fields.Float(string="Tarif 1", help="First different Public Sales Price")  # TARIF 1
    public_price_dif2 = fields.Float(string="Tarif 2", help="Second different Public Sales Price")  # TARIF 2
    public_price_dif3 = fields.Float(string="Tarif 3", help="Third different Public Sales Price")  # TARIF 3: missing in the list
    public_price_dif4 = fields.Float(string="Tarif 4", help="Forth different Public Sales Price")  # TARIF 4: missing in the list
    no_tax_price = fields.Float(string="Price without Tax", help="Sales Price without Taxes")  # TARIF HT
    page = fields.Char(string="Catalogue Page")  # PAGE: in the list not Integer (e.g.; XXXX), is it alright?
    origin = fields.Many2one('res.country', string="Country of Production")  # ORIGIN: not really a country in the list, maybe it's res.partner or just a char?
    weight = fields.Float(string="Weight")  # WEIGHT: missing the list!!!!! (uom_id can be used instead? In the list we have UNIT!)
    kg = fields.Boolean(string="KG")  # TO BE DISCUSSED (weight_uom_name can be used instead?), KG: missing in the list
    long_description = fields.Text()  # LONGDESCRIPTION: missing in the list, can be used as description, description_sale, etc?
    fam_web = fields.Text(string='WEB Family')  # TO BE DISCUSSED
    compatibility = fields.Text()  # can be also Char of HTML

