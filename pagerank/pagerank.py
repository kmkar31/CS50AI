import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    links = corpus[page]
    visit = dict()
    if len(links)!=0:
    	for page in corpus:
    		visit[page] = (1 - damping_factor)/len(corpus)
    	for page in links:
    		visit[page] = damping_factor/len(links)
    else:
    	for page in corpus:
    		visit[page] = 1/len(corpus)
    return visit



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Current_page takes the value of the starting page with an evenly distributed probability
    current_page = ''.join(random.choices(list(corpus.keys())))
    PageRank = dict(zip(list(corpus.keys()),[0]*len(corpus)))
    for i in range(n):
    	next_page_options = transition_model(corpus,current_page,damping_factor)
    	current_page = ''.join(random.choices(list(next_page_options.keys()),weights=list(next_page_options.values())))
    	if current_page in PageRank.keys():
    		PageRank[current_page] += 1/n
    	else:
    		PageRank[current_page] = 1/n
    return PageRank

def get_sum(corpus, PageRank, page, damping_factor):
    result = 0
    for p in corpus:
        if page in corpus[p]:
            result += PageRank[p] / len(corpus[p])
    result *= damping_factor

    result += (1-damping_factor)/len(corpus)
    
    return result

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    PageRank = {}.fromkeys(corpus.keys(), 1.0 /len(corpus))
    iterate = True
    while iterate:
        old_PageRank = copy.deepcopy(PageRank)
        for page in corpus:
            PageRank[page] = get_sum(corpus, PageRank, page,damping_factor)
        iterate = max([abs(old_PageRank[x]-PageRank[x]) for x in corpus])>=0.001
    return PageRank


if __name__ == "__main__":
    main()
