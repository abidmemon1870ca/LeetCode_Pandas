import pandas as pd
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    table = pd.DataFrame(student_data, columns = ['student_id','age'])
    return table