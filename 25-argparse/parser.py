import argparse

# description: for the text that is shown before the help text
# epilog: for the text shown after the help text

# Create the parser
my_parser = argparse.ArgumentParser(prog='myls',
                                    usage='%(prog)s [options] path',
                                    description='List the content of a folder')