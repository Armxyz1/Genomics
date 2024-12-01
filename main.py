import argparse
from process_data import get_data
from align.align_reads import align_reads
from clean_data import cleanup

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read Matching')

    parser.add_argument('--bwt', type=str, help='BWT file path', default='gene_data/chrX_last_col.txt')
    parser.add_argument('--map', type=str, help='Character Map file path', default='gene_data/chrX_map.txt')
    parser.add_argument('--ref', type=str, help='Reference Sequence file path', default='gene_data/chrX.fa')
    parser.add_argument('--reads', type=str, help='Reads file path', default='gene_data/reads')
    parser.add_argument('--err_thresh', type=int, help='Error Threshold', default=2)

    args = parser.parse_args()

    bwt_path = args.bwt
    map_path = args.map
    fa_path = args.ref
    reads_path = args.reads
    err_thresh = args.err_thresh

    print("Reading Data...")
    bwt, len_n, idx, reference, reads = get_data(bwt_path, map_path, fa_path, reads_path)
    print("Data Read Successfully!")
    print()

    print("Aligning Reads...")

    align_reads(bwt, len_n, idx, reference, reads, err_thresh)

    print("Reads Aligned Successfully!")
    print()
    print("Cleaning Data...")
    cleanup()
    print("Data Cleaned Successfully!")
    print()
    print("Output saved to processed_reads.csv")




    
