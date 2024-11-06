# my_odoo_project
# Odoo 11 Contracts Module

This project contains a custom Odoo 11 module for managing contracts, along with a Docker setup for easy deployment and development.

## Project Structure
my_odoo_project/
├── addons/
│   └── contracts/
│       ├── models/
│       │   ├── init.py
│       │   ├── contract.py
│       │   ├── contract_line.py
│       │   └── contract_payment.py
│       ├── views/
│       │   └── contract_views.xml
│       ├── wizards/
│       │   ├── init.py
│       │   ├── payment_wizard.py
│       │   └── payment_wizard_views.xml
│       ├── security/
│       │   └── ir.model.access.csv
│       ├── init.py
│       └── manifest.py
├── config/
│   └── odoo.conf
├── logs/
│   └── odoo-server.log
├── docker-compose.yml
├── Dockerfile
└── README.md


## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone this repository:

2. Build and start the containers:


3. Access Odoo:
- Open a web browser and go to `http://localhost:8069`
- Create a new database
- Install the Contracts module

## Contracts Module Features

- Manage contracts with details such as name, date of birth, and payment status
- Track contract lines with language, formalized language, and value-added tax
- Record payments for contracts
- Automatically update contract status based on payments

## Development

To make changes to the Contracts module:

1. Modify the files in the `addons/contracts/` directory
2. Restart the Odoo container:
3. Update the module in Odoo (Apps > Contracts > Update)

## Database Management

- Access pgAdmin at `http://localhost:5050`
- Login with:
- Email: admin@example.com
- Password: adminpassword

## Logs

Odoo logs are available in the `logs/odoo-server.log` file.

## Troubleshooting

If you encounter any issues:

1. Check the logs:
1. Ensure all containers are running:
3. Rebuild the containers if necessary:

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the LGPL-3 - see the LICENSE.md file for details.