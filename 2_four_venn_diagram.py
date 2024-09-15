from venny4py.venny4py import *
import csv
import pandas as pd
def create_figure1():
    path="./"
    dvf_virus = set(pd.read_csv(path+'dvf_virus.csv')["contig"])
    # print(dvf_virus)
    genomad_virus = set(pd.read_csv(path+"genomad_virus.csv")["contig"])
    viralm_virus = set(pd.read_csv(path+"viralm_virus.csv")["contig"])
    vs2_virus = set(pd.read_csv(path+"vs2_virus.csv")["contig"])

    # dict of sets
    sets = {
        'DeepVirFinder': dvf_virus,
        'VirSorter2': vs2_virus,
        'ViraLM': viralm_virus,
        'geNomad': genomad_virus
    }

    venny4py(sets=sets, out='Example_output')

# create_figure1()