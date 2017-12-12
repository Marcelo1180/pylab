#!/bin/bash
original_string='I love Suzy and Mary'
string_to_replace_Suzy_with='Sara'
result_string="${original_string/Suzy/$string_to_replace_Suzy_with}"
echo "$result_string"
