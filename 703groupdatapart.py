{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6b3c01dc",
   "metadata": {},
   "source": [
    "# Library"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fd50187e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Looking in indexes: https://bcms.bloomberg.com/pip/simple\n",
      "Requirement already satisfied: blpapi in /opt/anaconda3/lib/python3.8/site-packages (3.16.5)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install --index-url=https://bcms.bloomberg.com/pip/simple blpapi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "79ecdf01",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pandas_datareader import data\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "321bfadc",
   "metadata": {},
   "source": [
    "# Import data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e8cb3742",
   "metadata": {},
   "outputs": [],
   "source": [
    "time_interval = ['2016-01-01','2020-12-31']  # subject to change later\n",
    "df = data.get_data_yahoo(['AMD','AAPL','NVDA','MSFT','TSLA','FB','PYPL','BABA','INTC','ATVI','TTD','CRM','AMZN','MTCH','EA','GOOG','ZG','YELP'],start = time_interval[0],end = time_interval[1])['Adj Close']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8de3b2ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Symbols       AMD      AAPL      NVDA      MSFT      TSLA        FB      PYPL  \\\n",
      "Symbols                                                                         \n",
      "AMD      1.000000  0.979192  0.897232  0.960568  0.870288  0.883739  0.952427   \n",
      "AAPL     0.979192  1.000000  0.948611  0.957774  0.888106  0.928554  0.964113   \n",
      "NVDA     0.897232  0.948611  1.000000  0.886282  0.856425  0.935754  0.923414   \n",
      "MSFT     0.960568  0.957774  0.886282  1.000000  0.760154  0.906656  0.967400   \n",
      "TSLA     0.870288  0.888106  0.856425  0.760154  1.000000  0.780313  0.839221   \n",
      "FB       0.883739  0.928554  0.935754  0.906656  0.780313  1.000000  0.936565   \n",
      "PYPL     0.952427  0.964113  0.923414  0.967400  0.839221  0.936565  1.000000   \n",
      "BABA     0.834873  0.885273  0.931918  0.885699  0.701540  0.952497  0.898770   \n",
      "INTC     0.666300  0.686023  0.669975  0.816957  0.359897  0.729956  0.729664   \n",
      "ATVI     0.644676  0.742637  0.878367  0.669963  0.626572  0.809696  0.708580   \n",
      "TTD      0.946786  0.935234  0.851429  0.903829  0.906849  0.860336  0.943865   \n",
      "CRM      0.921137  0.929202  0.891888  0.954818  0.749056  0.904144  0.955459   \n",
      "AMZN     0.934124  0.947907  0.930859  0.967966  0.779375  0.917944  0.976255   \n",
      "MTCH     0.947442  0.938715  0.860008  0.970111  0.779274  0.893046  0.968904   \n",
      "EA       0.555902  0.653628  0.806499  0.601458  0.529733  0.794093  0.647350   \n",
      "GOOG     0.911192  0.939357  0.916509  0.957104  0.747949  0.945408  0.948504   \n",
      "ZG       0.788315  0.833598  0.880658  0.707312  0.909344  0.828334  0.806094   \n",
      "YELP    -0.381931 -0.311240 -0.136039 -0.316573 -0.375611 -0.103033 -0.276210   \n",
      "\n",
      "Symbols      BABA      INTC      ATVI       TTD       CRM      AMZN      MTCH  \\\n",
      "Symbols                                                                         \n",
      "AMD      0.834873  0.666300  0.644676  0.946786  0.921137  0.934124  0.947442   \n",
      "AAPL     0.885273  0.686023  0.742637  0.935234  0.929202  0.947907  0.938715   \n",
      "NVDA     0.931918  0.669975  0.878367  0.851429  0.891888  0.930859  0.860008   \n",
      "MSFT     0.885699  0.816957  0.669963  0.903829  0.954818  0.967966  0.970111   \n",
      "TSLA     0.701540  0.359897  0.626572  0.906849  0.749056  0.779375  0.779274   \n",
      "FB       0.952497  0.729956  0.809696  0.860336  0.904144  0.917944  0.893046   \n",
      "PYPL     0.898770  0.729664  0.708580  0.943865  0.955459  0.976255  0.968904   \n",
      "BABA     1.000000  0.798527  0.835631  0.783287  0.900006  0.907107  0.848184   \n",
      "INTC     0.798527  1.000000  0.591422  0.519500  0.792379  0.782231  0.756088   \n",
      "ATVI     0.835631  0.591422  1.000000  0.519102  0.679429  0.752646  0.623555   \n",
      "TTD      0.783287  0.519500  0.519102  1.000000  0.884235  0.893003  0.943296   \n",
      "CRM      0.900006  0.792379  0.679429  0.884235  1.000000  0.968882  0.949244   \n",
      "AMZN     0.907107  0.782231  0.752646  0.893003  0.968882  1.000000  0.951100   \n",
      "MTCH     0.848184  0.756088  0.623555  0.943296  0.949244  0.951100  1.000000   \n",
      "EA       0.826460  0.596329  0.940215  0.413476  0.617790  0.687241  0.553261   \n",
      "GOOG     0.934174  0.834039  0.766638  0.896306  0.952162  0.952154  0.941676   \n",
      "ZG       0.756906  0.411103  0.748906  0.823918  0.741672  0.769775  0.740425   \n",
      "YELP    -0.024338  0.021730  0.140447 -0.577137 -0.206919 -0.227700 -0.269589   \n",
      "\n",
      "Symbols        EA      GOOG        ZG      YELP  \n",
      "Symbols                                          \n",
      "AMD      0.555902  0.911192  0.788315 -0.381931  \n",
      "AAPL     0.653628  0.939357  0.833598 -0.311240  \n",
      "NVDA     0.806499  0.916509  0.880658 -0.136039  \n",
      "MSFT     0.601458  0.957104  0.707312 -0.316573  \n",
      "TSLA     0.529733  0.747949  0.909344 -0.375611  \n",
      "FB       0.794093  0.945408  0.828334 -0.103033  \n",
      "PYPL     0.647350  0.948504  0.806094 -0.276210  \n",
      "BABA     0.826460  0.934174  0.756906 -0.024338  \n",
      "INTC     0.596329  0.834039  0.411103  0.021730  \n",
      "ATVI     0.940215  0.766638  0.748906  0.140447  \n",
      "TTD      0.413476  0.896306  0.823918 -0.577137  \n",
      "CRM      0.617790  0.952162  0.741672 -0.206919  \n",
      "AMZN     0.687241  0.952154  0.769775 -0.227700  \n",
      "MTCH     0.553261  0.941676  0.740425 -0.269589  \n",
      "EA       1.000000  0.717074  0.708836  0.216984  \n",
      "GOOG     0.717074  1.000000  0.756859 -0.121972  \n",
      "ZG       0.708836  0.756859  1.000000 -0.123288  \n",
      "YELP     0.216984 -0.121972 -0.123288  1.000000  \n"
     ]
    }
   ],
   "source": [
    "corr_mat = df.corr()\n",
    "print(corr_mat)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57980bbc",
   "metadata": {},
   "source": [
    "## Pick our the highest correlation for each ETF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9099f1fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "np.fill_diagonal(corr_mat.values,np.nan)\n",
    "adj_corr = corr_mat.abs()\n",
    "s = adj_corr.unstack() \n",
    "s1 = s.sort_values().dropna()\n",
    "a = list(s1.idxmax())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "315bc96a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Symbols           AAPL        AMD\n",
      "Date                             \n",
      "2016-01-04   24.251431   2.770000\n",
      "2016-01-05   23.643709   2.750000\n",
      "2016-01-06   23.181013   2.510000\n",
      "2016-01-07   22.202665   2.280000\n",
      "2016-01-08   22.320068   2.140000\n",
      "...                ...        ...\n",
      "2020-12-24  131.161423  91.809998\n",
      "2020-12-28  135.852509  91.599998\n",
      "2020-12-29  134.043640  90.620003\n",
      "2020-12-30  132.900696  92.290001\n",
      "2020-12-31  131.877014  91.709999\n",
      "\n",
      "[1259 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "new_data = data.get_data_yahoo([a[0],a[1]],start = time_interval[0],end = time_interval[1])['Adj Close']\n",
    "print(new_data)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
