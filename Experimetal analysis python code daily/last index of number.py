{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "84cba39a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def lastindex(arr, x):\n",
    "    l = len(arr)\n",
    "    if l == 0:\n",
    "        return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb39a963",
   "metadata": {},
   "outputs": [],
   "source": [
    " smalleroutput = arr[1:]\n",
    "    print(smalleroutput)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0e9a95d",
   "metadata": {},
   "outputs": [],
   "source": [
    "smallerlistoutput = lastindex(smalleroutput, x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32ce3c76",
   "metadata": {},
   "outputs": [],
   "source": [
    "if smallerlistoutput != -1:\n",
    "        print(smallerlistoutput , end='_A_')              #test - 1\n",
    "        print(smallerlistoutput + 1, end='ha')             #test - 2\n",
    "        return smallerlistoutput + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f884b76a",
   "metadata": {},
   "outputs": [],
   "source": [
    "else:\n",
    "        if arr[0] == x:\n",
    "            return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25cbce6f",
   "metadata": {},
   "outputs": [],
   "source": [
    " else:\n",
    "            return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c404012",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sys import setrecursionlimit\n",
    "\n",
    "setrecursionlimit(11000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ccb45e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "n = int(input('Input Range:'))\n",
    "arr = list(int(i) for i in input('Array List:').strip().split(' '))\n",
    "x = int(input('To Find last index Number:'))\n",
    "print(lastindex(arr, x))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc35ba5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Input Range:5\n",
    "Array List:2 3 5 2 3\n",
    "To Find last index Number:3\n",
    "\n",
    "\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc8bfc6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "[3, 5, 2, 3]\n",
    "[5, 2, 3]\n",
    "[2, 3]\n",
    "[3]\n",
    "[]\n",
    "\n",
    "Answer  = 0_A_1ha1_A_2ha2_A_3ha3_A_4ha ----> 4\n",
    "'''"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
