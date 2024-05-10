// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
import "./1.sol";


contract StorageFactory is SimpleStorage{

    SimpleStorage[] public simpleStorageArray;
    function createSimpleStorageContract() public {
        SimpleStorage simStorage = new SimpleStorage();
        simpleStorageArray.push(simStorage);

    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber)  public {
        // We need contract of simpleStorage and ABI
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
    }

    function sfget(uint256 _simpleStorageIndex) public view returns(uint256){
         return SimpleStorage(address(simpleStorageArray[_simpleStorageIndex])).retrive();
    }

}
