import os
import pickle
import traceback
from sentence_transformers import SentenceTransformer

import constants
from dynamoUtilities import DynamoUtilities


class TrainModel:
    def __init__(self):
        self.dynamo_obj = DynamoUtilities(access_key_id=constants.aws_access_key_id, secret_access_key=constants.aws_secret_access_key, session_key=constants.aws_session_token)
        self.corpus, self.all_data = self.get_tagged_data_from_db()
        assert self.corpus!=[] and self.all_data!=[], "No data in DB!"

    def get_tagged_data_from_db(self):
        corpus, all_data = [], []
        try:
            db_data = self.dynamo_obj.get_data(constants.table_name)
            for each_data in db_data:
                if each_data["source_tag"].lower() != "others":
                    each_data["unix_timestamp"] = int(each_data["unix_timestamp"])
                    if not each_data["description"]:
                        corpus.append(each_data["title"])
                    else:
                        corpus.append(each_data["description"])
                    all_data.append(each_data)
            print("Prepared corpus of {0} documents!".format(len(corpus)))
        except Exception as e:
            print("Error: {0}\nException: {1}".format(e, traceback.format_exc()))
        return corpus, all_data

    def main(self):
        embedder = SentenceTransformer('all-MiniLM-L6-v2')
        corpus_embeddings = embedder.encode(self.corpus, convert_to_tensor=True, show_progress_bar=True)

        # import pdb; pdb.set_trace()
        # embedder.save(constants.model_output_folder + constants.model_file_name)
        if not os.path.exists(constants.model_output_folder):
            os.mkdir(constants.model_output_folder)
        print("Model created.. Dumping..")
        with open(constants.model_output_folder + constants.model_file_name, "wb") as fp:
            pickle.dump({'sentences': self.corpus, 'embeddings': corpus_embeddings, "metadata":self.all_data}, fp)
        # with open(constants.model_output_folder + constants.corpus_file_name, "wb") as fp:
        #     pickle.dump(self.corpus, fp)
        # with open(constants.model_output_folder + constants.metadata_file_name, "wb") as fp:
        #     pickle.dump(self.all_data, fp)

if __name__ == "__main__":
    TrainModel().main()