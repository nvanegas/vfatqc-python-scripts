from gempython.utils.standardopts import parser

parser.add_option("--ztrim", type="float", dest="ztrim", default=0.0,
                  help="Specify the p value of the trim", metavar="ztrim")
parser.add_option("--scanmin", type="int", dest="scanmin",
                  help="Minimum value of scan parameter", metavar="scanmin", default=0)
parser.add_option("--scanmax", type="int", dest="scanmax",
                  help="Maximum value of scan parameter", metavar="scanmax", default=254)
parser.add_option("--nevts", type="int", dest="nevts",
                  help="Number of events to count at each scan point", metavar="nevts", default=1000)
parser.add_option("--vfatmask", type="int", dest="vfatmask", 
                  help="VFATs to be masked in scan & analysis applications (e.g. 0xFFFFF masks all VFATs)", metavar="vfatmask", default=0x0)
