#!/usr/bin/python3
import os
import sys
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

  parser.add_argument("-f", "--filter", dest = "filter", default = [], type = \
    str, nargs = "+", help = "Filter specific domain, sub-dommain or indicator")

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
      titles.setdefault(domain, domain_title)

    if line[1]:
      subdomain, subdomain_title = line[1].split("]")[0][1:], line[1]
      titles.setdefault(subdomain, subdomain_title)
    
    ## Capture and model the relevant information for the plot
    indicator = line[2].split("]")[0][1:]
    ## Skip specific indicators for a given domain/sub-domain if filtered:
    if args.filter:
      domain = indicator.split(".")[0]
      subdomain = ".".join(indicator.split(".")[:2])
      if set([domain, subdomain, indicator]) & set(args.filter) == set():
        continue
    titles.setdefault(indicator, line[2])
    
    ## Expected Value
    expected = int(line[args.refColumn])
    values.setdefault(indicator, {}).setdefault("reference", expected)

    ## Self-Assessment values - evaluated against the expected value
    for pos in args.inColumns:
      selfAssessment = int(line[pos])
      if selfAssessment < expected:
        values[indicator]["lower"] = values[indicator].get("lower", 0) + 1
      elif selfAssessment == expected:
        values[indicator]["equal"] = values[indicator].get("equal", 0) + 1
      else:
        values[indicator]["higher"] = values[indicator].get("higher", 0) + 1
  
  ## Define some attributes for each category
  attributes = {
    "lower":  {"color": "#95DBE5FF", "legend": "Lower than expected"},
    "equal":  {"color": "#078282FF", "legend": "As expected"},
    "higher": {"color": "#339E66FF", "legend": "Higher than expected"},
  }
    
  ## Produce the plot
  fig, ax = plt.subplots( nrows = 1, ncols = 1, figsize = (18, 10))
 
  cumulative = []
  total = float(len(args.inColumns))
  keys = sorted(values.keys(), reverse = True)
  
  for categ in ["lower", "equal", "higher"]:
   
    x = [0 if not categ in values[indicator] else values[indicator][categ]/total \
      for indicator in keys]
    
    if not cumulative:
      cumulative = [0 for pos in range(len(x))]
  
    ax.barh(range(len(x)), x, align = 'center', left = cumulative, \
      color = attributes[categ]["color"], label = attributes[categ]["legend"])
        
    cumulative = [x[pos] + cumulative[pos] for pos in range(len(x))]
    
  ax.legend(fontsize = "x-large", ncol = 3, bbox_to_anchor=(0.75, 1.08), \
    loc = 1, fancybox=True, shadow=True)


  ax.set_yticks(range(len(keys)))
  ax.set_yticklabels([textwrap.shorten(titles[indicator], width = 60, \
    placeholder = " ...") for indicator in keys])
  ax.set_ylim([-.5, len(keys) - .5])

  ax.xaxis.grid(True, linestyle = "-.")
   
  ax.set_xticks([v/total for v in range(len(args.inColumns) + 1)])
  ax.set_xticklabels(range(len(args.inColumns) + 1))
  
  ax.set_xlabel('Number of FEGA Nodes at certain maturity level', \
    fontsize = "xx-large", weight = "bold")
  ax.set_ylabel('Indicators', fontsize = "xx-large", weight = "bold")

  plt.tight_layout() 
  plt.show()

  if args.outFile:
    name, extension = os.path.splitext(args.outFile)
    
    if not extension in [".png", ".svg", ".pdf"]:
      args.outFile += ".svg"

    fig.savefig(args.outFile, transparent = False, dpi = 450, \
      bbox_inches = "tight")
