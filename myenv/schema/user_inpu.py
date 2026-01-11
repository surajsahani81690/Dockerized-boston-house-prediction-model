from pydantic import BaseModel, Field
from typing import Annotated

class UserInput(BaseModel):
    CRIM: Annotated[float, Field(..., description="Crime rate per capita by town", example=[0.0063, 0.005])]
    ZN: Annotated[float, Field(..., description="Proportion of residential land zoned for lots over 25,000 sq.ft.", example=[18.0, 90.0, 100.0])]
    INDUS: Annotated[float, Field(..., description="Proportion of non-retail business acres per town", example=[2.31, 7.07])]
    CHAS: Annotated[int, Field(..., description="Charles River dummy variable (1 if tract bounds river; 0 otherwise)", example=[0, 1])]
    NOX: Annotated[float, Field(..., description="Nitric oxides concentration (parts per 10 million)", example=[0.538, 0.469])]
    RM: Annotated[float, Field(..., description="Average number of rooms per dwelling", example=[6.575, 7.185])]
    AGE: Annotated[float, Field(..., description="Proportion of owner-occupied units built prior to 1940", example=[65.2, 45.4])]
    DIS: Annotated[float, Field(..., description="Weighted distances to five Boston employment centres", example=[4.09, 6.062])]
    RAD: Annotated[int, Field(..., description="Index of accessibility to radial highways", example=[1, 24])]
    TAX: Annotated[float, Field(..., description="Full-value property-tax rate per $10,000", example=[296.0, 666.0])]
    PTRATIO: Annotated[float, Field(..., description="Pupil-teacher ratio by town", example=[15.3, 20.2])]
    B: Annotated[float, Field(..., description="1000(Bk - 0.63)^2 where Bk is the proportion of Black population", example=[396.9, 390.5])]
    LSTAT: Annotated[float, Field(..., description="% lower status of the population", example=[4.98, 12.43])]
