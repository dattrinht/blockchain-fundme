// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MockV3Aggregator {

    uint8 public decimals;
    int256 public price;

    constructor(
        uint8 _decimals,
        int256 _price
    ) public {
        decimals = _decimals;
        price = _price;
    }

    function latestRoundData()
        external
        view
        returns (
        uint80 roundId,
        int256 answer,
        uint256 startedAt,
        uint256 updatedAt,
        uint80 answeredInRound
        )
    {
        return (
        0,
        price,
        0,
        0,
        0
        );
    }
}