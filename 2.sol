// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract mycontract {
    struct People {
        uint256 pid;
        string name;
    }

    People public person = People({pid: 123, name: "Sharath"});
    People[] public people; // dynamic array
    mapping(string => uint256) public nametonumber;
    // People[3] public people; // fixed array

    // 2 ways to store variables
    //memory or storage
    //memory will only be stored during execution
    function addperson(string memory name, uint256 pid) public {
        people.push(People(pid, name));
        nametonumber[name] = pid;
    }
}
