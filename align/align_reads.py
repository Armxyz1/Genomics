from support import *
from rank import SuccinctRank
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")
from multiprocessing import Pool, cpu_count


next_char = {'A': 'C', 'C': 'G', 'G': 'T', 'T': '$'}

def align_reads(bwt, n, idx, reference, reads, err_thresh):

    print("Initialising Succinct Rank...")
    rk_A = SuccinctRank(bwt,'A')
    rk_C = SuccinctRank(bwt,'C')
    rk_G = SuccinctRank(bwt,'G')
    rk_T = SuccinctRank(bwt,'T')
    print()

    agg_val = {
        'A': 0,
        'C': rk_A.rank(n), 
        'G': rk_A.rank(n)+rk_C.rank(n), 
        'T': rk_A.rank(n)+rk_C.rank(n)+rk_G.rank(n), 
        '$': rk_A.rank(n)+rk_C.rank(n)+rk_G.rank(n)+rk_T.rank(n)
        }
    
    rk_dict = {'A': rk_A, 'C': rk_C, 'G': rk_G, 'T': rk_T}

    reads = list(enumerate(reads))
    progress = tqdm(total=len(reads))

    # with Pool(cpu_count()) as p:
    #     p.map(process_read, [(read, idx, reference, rk_dict, agg_val, err_thresh, progress) for read in reads])

    for part in range(0, len(reads), 100):
        with Pool(cpu_count()) as p:
            p.map(process_read, [(read, idx, reference, rk_dict, agg_val, err_thresh, progress) for read in reads[part:part+100]])


    
    
    
    

