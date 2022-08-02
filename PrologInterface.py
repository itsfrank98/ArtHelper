from pyswip import Prolog
import os


class PrologInterface():
    def __init__(self, kb_path='kb'):
        self.prolog = Prolog()
        self.kb_path = kb_path
        for f in os.listdir(kb_path):
            if f.endswith('.pl'):
                self.prolog.consult(os.path.join(kb_path, f))

    def get_kb_path(self):
        return self.kb_path

    def query(self, query):
        """
        Runs the desired query, returning both the results and the explanations.
        :param query: Query to run
        :return: results
        """
        results = {}
        results['query_results'] = list(self.prolog.query(query))
        results['explanations'] = list(self.prolog.query("used(X)"))[0]['X']
        self.prolog.query("retractall(used(X))")    # We retract everything regarding the explanations, because the explanations provided for the current query will not be useful for the next one
        return results
