// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0; // specifying the version to use

contract SimpleStorage {
    // uint, int, int256, uint256
    // bool
    // string
    // address
    uint public favnumber = 5; // public key defines the visibility of variables. external, public, internal, private
    // by default the visibility will be internal/ public variables will have a view function by default
    int num = 5;
    bool boolean = true;
    string strings = "let it be";
    int256 num1 = -5;
    // address favoriteadress = 0xe4fb25c80ce8275b2052374c62f77899ba4a15f5;
    bytes32 favbyte = "Dog"; //max size bytes64
    int num2; //this will get initialized to zero

    // function call or state changes will be called as trancactions
    function store(uint number) public {
        favnumber = number;
    }

    // view functions don't make any changes or transactions. It will only read and returns. view/pure
    function retrive() public view returns (uint) {
        return favnumber;
    }

    // view and pure will have blue buttons since it won't make any changes or transactions
    function add(uint n) public pure returns (uint) {
        return (n + n);
    }
}
