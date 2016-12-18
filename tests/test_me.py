# -*- encoding: utf-8 -*-
# Aparecium is also called REVEALING SPELL. As of HarryPotter, this can reveal any invisible things.

from alohomora import Alohomora as Fun
import pytest

# ------------------------------------------------
# Checking with Manually Computed Output
def test_no_blank_words_true():
    fun = Fun()
    assert(fun.magic("edzlatsh", "hazel") == 1)

def test_no_blank_words_false():
    fun = Fun()
    assert(fun.magic("edzlatsh", "hazely") == 0)
# -------------------------------------------------

# Checking if I did missed giving proper inputs in MAGIC
def test_single_input_for_magic():
    fun = Fun()
    with pytest.raises(ValueError):
        fun.magic('Hey')

# Checking if I did missed giving proper inputs in LONGEST
def test_no_input_for_longest():
    fun = Fun()
    with pytest.raises(ValueError):
        fun.longest()

