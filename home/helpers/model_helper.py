# This file is used to store method of model helpers.

class ModelHelper:
    @staticmethod
    def user_directory_path(user_instance, filename):
        # Upload file to specific user folder media/<user_id><filename>
        return "user_{0}/{1}".format(user_instance.id, filename)
