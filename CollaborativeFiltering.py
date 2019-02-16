import pandas as pd
import gc

class CollaborativeFiltering:
    
    def __init__(self):
        
        self.data = pd.DataFrame()
        self.products = pd.Series()
        
    def load_data(self, file_path):
        """
        Loads the file from the given path. 
        Creates the data matrix and a pandas Series with the products names.
        
        Args:
            file_path: path of the file to be loaded.
            
        """
        
        df = pd.read_csv(file_path, engine = 'python')

        unique_tags = df.tag_id.unique()

        self.products = pd.Series(index = unique_tags, data = "")
        
        for tag in unique_tags:
            self.products[tag] = df[df.tag_id == tag].product_name.iloc[0]
        
        self.data = pd.DataFrame(data = 0, index = df.user_id.unique(), columns = unique_tags)

        for index, row in df.iterrows():
            self.data.loc[row["user_id"], row["tag_id"]] += 1
            
        del df
        gc.collect()
        
    def similar_items(self, tag_id, n = 10):
        """
        Calculates the items that have been viewed by other users that also viewed the given item.
        
        Args:
            tag_id: given item to be considered.
            n: maximum number of items returned.
            
        """
        tag_viewed_data = self.data[self.data[tag_id] == 1]

        sum_views = tag_viewed_data.sum().drop(tag_id)

        similar_tags = sum_views.sort_values(ascending = False).head(n)

        similar_tags = similar_tags[similar_tags > 0]
        
        return self.products[similar_tags.index]
    
    def most_viewed_items(self, n = 10):
        """
        Returns the most viewed items by all the users.
        
        Args:
            n: maximum number of items to be returned.
            
        """
        
        return self.data.sum().sort_values(ascending = False).head(n)