// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract Counter {
    uint256 public count; //unsigned integer

    //function to increment the count
    function increment() public {
        count = count + 1; // or count++;
    }

    function decrement() public returns (uint256 _decrease) {
        count--;
        return count;
    }
    //function to only read information from blockchain and not modify at all.
    //function to return number

    function getCount() public view returns (uint256) {
        return count;
    }
}
