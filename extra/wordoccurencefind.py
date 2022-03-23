from phrasefinder import phrasefinder as pf

def main():
    """
    Performs a simple request and prints out the result.
    """

    # Set up your query.
    
    query = str(input("Enter a word and get the percentage of books it is in: "))

    # Optional: set the maximum number of phrases to return.
    options = pf.SearchOptions()
    options.topk = 10

    # Send the request.
    try:
        result = pf.search(pf.Corpus.AMERICAN_ENGLISH, query, options)
        if result.error:
            print('Request was not successful: {}'.format(result.error['message']))
            return

        # Print phrases line by line.
        for phrase in result.phrases:
            print('{0:6f}'.format(phrase.score), end='')
            for term in phrase.terms:
                print(' {}'.format(term.text), end='')
            print()

    except Exception as error:
        print('Fatal error: {}'.format(error))

if __name__ == '__main__':
    main()
