#!/usr/bin/python3

import os
import sys
import random
import hashlib
import textwrap
import argparse
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

  parser = argparse.ArgumentParser()

  parser.add_argument("-i", "--in", dest = "inFile", required = True, type = \
    str, help = "Input self-evaluation file")

  parser.add_argument("-r", "--ref", dest = "refColumn", required = True, \
    type = int, help = "Indicate which column contains the reference values. "
    + "Starts in 0")
    
  parser.add_argument("-c", "--columns", dest = "inColumns", required = True, \
    type = int, nargs = "+", help = "Indicate which column/s contain the "
    + "self-assessment values. Starts in 0")
    
  parser.add_argument("-o", "--out", dest = "outFile", default = None, type = \
    str, help = "Set output filename")

  parser.add_argument("--no-header", dest = "header", action = 'store_false', \
    help = "Indicate there are no headers in the input file")

  args = parser.parse_args()

  ## Check input parameters
  if not os.path.isfile(args.inFile):
    sys.exit(("ERROR: Check input self-evaluation file '%s'") % (args.inFile))

  values = {}
  titles = {}
  for input_line in open(args.inFile, "r"):
    ## If input file has headers, discarded it
    if args.header:
      args.header = False
      continue
    
    ## Discard empty lines
    if not input_line.strip():
      continue
    
    ## If considered line does not have indicators - using [] - discard it.
    if input_line.find("[") == -1 or input_line.find("]") == -1:
      continue      
    
    ## Split and clean up each line
    line = list(map(str.strip, input_line.split("\t")))

    ## Capture domain and/or subdomains
    if line[0]:
      domain, domain_title = line[0].split("]")[0][1:], line[0]
    if line[1]:
      subdomain, subdomain_title = line[1].split("]")[0][1:], line[1]
    
    ## Capture and model the relevant information for the plot
    indicator = line[2].split("]")[0][1:]
    
    titles.setdefault(domain, domain_title)
    titles.setdefault(subdomain, subdomain_title)
    
    ## Expected Value
    expected = int(line[args.refColumn])
    values.setdefault(indicator, {}).setdefault("reference", expected)

    ## Self-Assessment values
    selfAssessment = [int(line[pos]) for pos in args.inColumns]
    values[indicator].setdefault("assessment", selfAssessment)
  
  ## Produce the plot
  fig, ax = plt.subplots( nrows = 1, ncols = 1, figsize = (18, 10))
  keys = sorted(values.keys())

  window = (1/float(len(args.inColumns))) * .8
   
  y_max = 0
  y_values = set()
  for pos in range(len(args.inColumns)):

    factor = pos/float(len(args.inColumns))
    y = [values[categ]["assessment"][pos] for categ in keys]
    x = [x + factor for x in range(len(y))]
    
    ax.bar(x, y, width = window, align = "edge", zorder = 5)
    y_max = max([y_max, max(y)])
    y_values |= set(y)

  ax.yaxis.grid(True, linestyle = "-.")
  ax.set_xlim([-.2, len(y) + .2])
  ax.set_ylim(ymax = y_max + .2)
  
  interv = x[0] + window  
  for pos in range(len(keys)):
    y = [values[keys[pos]]["reference"], values[keys[pos]]["reference"]]
    x = [pos, pos + interv]
    ax.plot(x, y, color = "black", linewidth = 2, zorder = 10)

  categories = {}
  for categ in keys:
    label = categ.replace("[", "").replace("]", "").split(".")
    categories.setdefault(label[0], {}).setdefault(label[1], []).append(categ)

  white = True
  x_values = []
  cumulative = 0 
  for major in sorted(categories):
    size = sum([len(categories[major][minor]) for minor in categories[major]])
    x_values.append(cumulative + (size/2))
    
    if not white:
      ax.bar([cumulative], [y_max + .2], width = size, alpha = 0.5, zorder = 1,
        align = "edge", color = "lightgrey")
      white = True
    else:
      white = False
    cumulative += size

  ax.set_xticks(x_values)
  ax.set_xticklabels([textwrap.shorten(titles[major], width = 24, \
    placeholder = " ...") for major in sorted(categories)])
  ax.set_yticks(sorted(y_values))

  plt.tight_layout() 
  plt.show()
