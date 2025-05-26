{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cc82862e-b3b7-4649-a3c1-4cc74bee0fbb",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ad5de7a5-2eae-432d-9366-49f123a03bc1",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9062676c-bceb-4ec9-b957-8d31467db8e5",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "url = \"https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-emplacement-des-stations/records?limit=100\"\n",
    "\n",
    "response = requests.get(url)\n",
    "\n",
    "data = response.json()\n",
    "records = data[\"results\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2ebcd1f9-6fd7-4767-8492-b7e9b1d60c99",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'dict' object has no attribute 'show'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[10], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdata\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mshow\u001b[49m()\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'dict' object has no attribute 'show'"
     ]
    }
   ],
   "source": [
    "rdd =  spark.createDataFrame(records)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PySpark",
   "language": "python",
   "name": "pyspark"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
