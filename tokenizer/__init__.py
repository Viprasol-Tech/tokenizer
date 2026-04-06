"""
tokenizer - Tokenize text into words and sentences

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import Tokenizer, tokenize, process, main

__all__ = ["Tokenizer", "tokenize", "process", "main"]
