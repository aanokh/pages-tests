from pyscript import sync

def load_data():
    import warnings
    # filter out pyarrow requirement warning (pyarrow is not ported to pyscript)
    warnings.filterwarnings('ignore')
    
    global pd
    if "pd" not in globals():
        import pandas as pd
    
    global difflib
    if "difflib" not in globals():
        import difflib

    global cosine_similarity
    if "cosine_similarity" not in globals():
        from sklearn.metrics.pairwise import cosine_similarity

    global TfidfVectorizer
    if "TfidfVectorizer" not in globals():
        from sklearn.feature_extraction.text import TfidfVectorizer
    
    global open_url
    if "open_url" not in globals():
        from pyodide.http import open_url

    url_content = open_url("https://raw.githubusercontent.com/aanokh/Summer_Project/77ea6ed11e2d754d8e0a1a8b5ea130daa8627076/Book_Details.csv")
    book_data = pd.read_csv(url_content)
    book_data = book_data.reset_index()

    sync.hello()
    