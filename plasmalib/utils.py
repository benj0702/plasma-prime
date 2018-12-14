from web3 import Web3
from web3.contract import ConciseContract
from eth_tester import EthereumTester, PyEVMBackend
from vyper import compiler
from math import floor, ceil, log
from hexbytes import HexBytes
from plasmalib.constants import *
from eth_utils import encode_hex as encode_hex_0x
from eth_utils import (
    int_to_big_endian,
)


def int_to_big_endian_of_size(size):
    def justified_big_endian(val):
        return int_to_big_endian(val).rjust(size, b'\0')
    return justified_big_endian

int_to_big_endian4 = int_to_big_endian_of_size(4)
int_to_big_endian8 = int_to_big_endian_of_size(8)
int_to_big_endian12 = int_to_big_endian_of_size(12)
int_to_big_endian32 = int_to_big_endian_of_size(32)

def addr_to_bytes(addr):
    return bytes.fromhex(addr[2:])

def to_bytes32(i):
    return i.to_bytes(32, byteorder='big')

def bytes_to_int(value):
    return int.from_bytes(value, byteorder='big')

def encode_hex(n):
    if isinstance(n, str):
        return encode_hex(n.encode('ascii'))
    return encode_hex_0x(n)[2:]

def contract_factory(w3, source):
    bytecode = '0x' + compiler.compile(source).hex()
    abi = compiler.mk_full_signature(source)
    return w3.eth.contract(abi=abi, bytecode=bytecode)
