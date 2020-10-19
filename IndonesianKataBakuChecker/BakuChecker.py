from .BaseChecker import *
import os.path, json

class BakuChecker(BaseChecker):
    def __init__(self, dict = None):
        super().__init__("Kata Baku Checker")
        self.dict = []
        self.prepared = False

        if (dict != None):
            self.prepareDict(dict)

    def prepareDict(self, path):
        if (not(os.path.exists(path))):
            print("File {} doesn't exist.".format(path))
            return

        for element in open(path).readlines():
            element = element.split("|")
            element[0] = element[0].strip().lower()
            element[1] = element[1].strip().lower()

            if (not(element in self.dict)):
                self.dict.append(element)

        self.prepared = True

    def slice(self, text, start, length, helperLength = 20):
        ret = ""
        ed = ""

        if (start>helperLength):
            ret += "..."
            st = start-helperLength
        else:
            st = 0

        if (start+length+helperLength < len(text)):
            ed += "..."
            end = start+length+helperLength
        else:
            end = len(text)

        return ret+text[st:end]+ed

    def check(self, text):
        if (not(self.prepared)):
            print("The dictionary is not prepared.")
            return []

        errList = []

        textLower = text.lower()

        for element in self.dict:
            i = 0

            while(textLower.find(element[1], i)!=-1):
                i = textLower.find(element[1], i)
                errList.append(ErrorMessage(self, self.slice(text, i, len(element[1])), "The correct word for '{}' is '{}'".format(element[1], element[0])))

                i += len(element[1])

        return errList


# check the word

class WordReader(BakuChecker):

    """
    This class make bakuchecker posibble to use as a package
    so you will easly use it in any python program
    """

    def read_file(self, f):
        dictFile = os.path.dirname(os.path.realpath(__file__))+"/dict.txt"
        checkerList = []
        checkerList.append(BakuChecker(dictFile))
        final_list = []
        for i in range(0, len(f)):
            errList = []

            if (f[i][len(f[i])-1]=="\n"):
                f[i] = f[i][:-1]

            for checker in checkerList:
                errList += checker.check(f[i])

            for err in errList:
                result_list = {}
                result_list['checker'] = err.checkerDescription
                result_list['line'] = i + 1
                result_list['original_text'] = err.original
                result_list['message'] = err.message
                final_list = result_list
                yield final_list

    def get_result(self, text):
        """
        this method used for get result of the word
        """
        parse_text = text.split('\n')
        return self.read_file(parse_text)