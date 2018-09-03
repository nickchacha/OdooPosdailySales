{
	'name': 'Point of Sale Dairy Report',
	'version': '10.0.1.0.0',
    'summary': """Daily Sales Report """,
    'description': """Report to generate Sales Per day""",
    'author': 'Chacha Kairu',
    'company': 'Fastworld Solutions',
    'website': 'http://www.fastworldsolutions.net',
    'category': 'Generic Modules/Point Of Sale',
    'depends': ['stock_account', 'barcodes', 'web_editor','point_of_sale'],
    'license': 'LGPL-3',
	'application': True,
	'data':[
		'views/pos_dairyorders_report_view.xml'],
}