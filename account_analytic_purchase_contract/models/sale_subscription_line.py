from openerp import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)


class sale_subscription_line(models.Model):
    _inherit = ['sale.subscription.line']

    # Already (bad labelled) existing field
    analytic_account_id = fields.Many2one('sale.subscription', string='Subscription', ondelete='cascade')

    # New (right labelled) field for AA
    impacted_analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account")
