
#USAGE: python3 get_gene_coords.py path_to_gff_file gene_name
#EXAMPLE: python3 get_gene_coords.py Downloads/Cp3488.genes.gff3 CPAG_00216

def get_gene_coords(gff_path, gene_name):

    """ Reads gff lines containing given gene name and returns coordinate info of the gene
    """

    gene_info = None

    #opening file in read-only mode and reading line by line
    f = open(gff_path, 'r')
    for line in f.readlines():

        if gene_name in line:

            #information fields in GFFs are separated by tabs,
            #split up the information into a list based on where the tabs are
            parsed = line.split('\t')

            feature = parsed[2]

            if feature == 'gene':

                #get the parts of the line that we care about
                contig = parsed[0]

                #the computer thinks these are strings unless I specify that they are integers
                start, stop =  int(parsed[3]), int(parsed[4])

                direction = parsed[6]

                gene_info = [contig, start, stop, direction]

                break #we found what we need so we don't need to go through the rest of the file
                      #in practice, it's a good idea to go through the rest of the file and
                        #check that there aren't duplicate entries

    if gene_info == None:
        print('gene not found')
        return None

    print('contig: {}, start: {}, stop: {}, direction: {}'.format(contig, start, stop, direction))

    return gene_info


##### parsing the command line input
import sys

gff_path = sys.argv[1]
gene_name = sys.argv[2]

if __name__ == '__main__': #means we're calling the script directly from the command line

    get_gene_coords(gff_path, gene_name)
