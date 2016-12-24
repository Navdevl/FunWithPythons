# -*- encoding: utf-8 -*-
# Aparecium is also called REVEALING SPELL. As of HarryPotter, this can reveal any invisible things.

from alohomora import Alohomora as Fun
import pytest

# ------------------------------------------------
# Checking with Manually Computed Output
def test_no_blank_words_true():
    fun = Fun("edzlatsh", "hazel")
    assert(fun.magic() == 1)

def test_no_blank_words_false():
    fun = Fun("edzlatsh", "hazely")
    assert(fun.magic() == 0)
# -------------------------------------------------

# Checking if I did missed giving proper inputs in MAGIC
def test_single_input_for_magic():
    fun = Fun('Hey')
    with pytest.raises(ValueError):
        fun.magic()

# Checking if I did missed giving proper inputs in LONGEST
def test_no_input_for_longest():
    fun = Fun()
    with pytest.raises(ValueError):
        fun.longest()

