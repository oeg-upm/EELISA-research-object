import argparse

if __name__ == "__main__":

    #----------------------------------------------------------------------------------
    # Handle arguments
    #----------------------------------------------------------------------------------

    parser = argparse.ArgumentParser(
        description='Human and machine readeable input as a yalm file and create RO-Object in jsonld and/or HTML view.')

    # Required positional argument
    parser.add_argument('-i', type=str, required=True, metavar='INPUT_FILE',
        help='Path of the required yalm input. Follow the documentation or the example given to see the structure of the file.')

    # Optional argument
    parser.add_argument('--output_directory', type=str, help='Output diretory.')
    
    # Optional argument
    parser.add_argument('--properties_file', type=str, help='Properties file name.')

    args = parser.parse_args()

    # Default values and yalm_input
    output_directory = "output" if args.output_directory is None else args.output_directory
    properties_file = "resources/properties.yaml" if args.properties_file is None else args.properties_file
    input_yalm = args.i

    #----------------------------------------------------------------------------------
    # Create RO objects and dump results
    #----------------------------------------------------------------------------------
    
    import Properties

    Properties.init(properties_file, input_yalm, output_directory)

    from Ro_html import Ro_html

    ro_html = Ro_html()
    ro_html.createHTML_file()

    from Ro_jsonld import Ro_jsonld

    ro_jsonld = Ro_jsonld()
    ro_jsonld.createJSONLD_file()

