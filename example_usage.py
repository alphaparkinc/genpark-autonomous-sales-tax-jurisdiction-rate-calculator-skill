from client import AutonomousSalesTaxJurisdictionRateCalculatorClient

def main():
    client = AutonomousSalesTaxJurisdictionRateCalculatorClient()
    res = client.calculate_sales_tax_and_nexus(250.0, {'city': 'New York', 'state': 'NY', 'zip': '10001'})
    print('Tax ID: ' + res['tax_calculation_id'] + ' | Jurisdiction: ' + res['destination_jurisdiction'])
    print('Subtotal: $' + str(res['cart_subtotal_usd']) + ' -> Tax Due: $' + str(res['sales_tax_due_usd']) + ' (' + str(res['effective_tax_rate_pct']) + '%)')
    print('Nexus: ' + res['nexus_determination'] + ' | Auto-Filing: ' + str(res['auto_filing_remittance_ready']))

if __name__ == '__main__':
    main()
