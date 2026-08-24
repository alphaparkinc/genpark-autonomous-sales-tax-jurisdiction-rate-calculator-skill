class AutonomousSalesTaxJurisdictionRateCalculatorClient:
    def calculate_sales_tax_and_nexus(self, cart_subtotal_usd=150.0, ship_to_address=None, origin_state='CA'):
        ship_to_address = ship_to_address or {'city': 'Austin', 'state': 'TX', 'zip': '78701'}
        jurisdiction_tax_rates = {
            'TX': {'state_rate': 0.0625, 'local_rate': 0.0200, 'nexus_status': 'ECONOMIC_NEXUS_ESTABLISHED'},
            'CA': {'state_rate': 0.0725, 'local_rate': 0.0150, 'nexus_status': 'PHYSICAL_NEXUS_ESTABLISHED'},
            'NY': {'state_rate': 0.0400, 'local_rate': 0.04875, 'nexus_status': 'ECONOMIC_NEXUS_ESTABLISHED'}
        }
        tax_rule = jurisdiction_tax_rates.get(ship_to_address.get('state', 'TX'), jurisdiction_tax_rates['TX'])
        combined_rate = tax_rule['state_rate'] + tax_rule['local_rate']
        tax_due = round(cart_subtotal_usd * combined_rate, 2)
        return {
            'tax_calculation_id': 'num_tax_99182',
            'destination_jurisdiction': ship_to_address.get('state', 'TX') + ' (' + ship_to_address.get('zip', '78701') + ')',
            'cart_subtotal_usd': cart_subtotal_usd,
            'effective_tax_rate_pct': round(combined_rate * 100, 3),
            'sales_tax_due_usd': tax_due,
            'nexus_determination': tax_rule['nexus_status'],
            'auto_filing_remittance_ready': True
        }
