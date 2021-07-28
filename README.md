# Mail PDF Printer

A simple script to print PDF files attached in your emails.

## Config

The config of this script is passed via environment variables, you can do that either supplying them manually or using
a `config.env` file for which an example is provided under the `config` directory.

The environment variables this script uses are:

| NAME            | DESCRIPTION                                      |
| --------------- | ------------------------------------------------ |
| ORG_EMAIL       | Your organization email                          |
| USER_NAME       | Username of email account                        |
| PASSWORD        | Password of email account                        |
| SERVER_URI      | The uri to the IMAP service                      |
| SERVER_PORT     | The port for IMAP                                |
| PREFIX_TO_PRINT | The prefix for the emails that should be printed |
| PRINTER_NAME    | The name of the printer which will be used       |

### Using `config.env` file

The `config` directory should exist at the same level as the `src` directory or one level above the `execution path` of
the script.

> :warning: Note that this script will try first to get the `config.env` values for the variables and then **overwrite** them with the values supplied from the environment if they exist.

### Using the `config.env` AND the `Docker` Image provided

The config directory should be mapped to `/config` directory.

#### Example

```bash
docker run -it -v $(pwd)/config:/config -e USER_NAME=USERNAME mail_pdf_printer
```
