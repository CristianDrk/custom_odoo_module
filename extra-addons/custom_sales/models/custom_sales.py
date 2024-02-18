from odoo import models, fields, api, _
from odoo.exceptions import UserError

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains('order_line')
    def _check_product_quantity(self):
        for order in self:
            if any(line.product_uom_qty <= 0 for line in order.order_line):
                raise UserError(_("You cannot confirm a sale order with product quantities equal to zero."))
    
    def remove_zero_quantity_lines(self):
        #Busca las líneas con 0 productos y llama al método unlink para borrarlas
        lines_to_remove = self.order_line.filtered(lambda line: line.product_uom_qty == 0)
        lines_to_remove.unlink()