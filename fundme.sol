// SPDX-License-Identifier: MIT
pragma solidity >=0.6.6 <=0.9.0;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

// Aim is to accept some type of payment and keep the track of which address funded how much
contract FundMe {
    using SafeMathChainlink for uint256;
    address[] public funders;
    address public owner;

    constructor() {
        owner = payable(msg.sender);
    }

    mapping(address => uint256) public addressToAmountFunded;
    function fund() public payable {
        uint256 minimumUSD = 0.01 * 10 ** 18;
        require(
            getConverstedPrice(msg.value) >= minimumUSD,
            "You need to spend more eth"
        );
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0x694AA1769357215DE4FAC081bf1f309aDC325306
        );
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0x694AA1769357215DE4FAC081bf1f309aDC325306
        );
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }

    function getConverstedPrice(
        uint256 ethAmount
    ) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 etherPriceInUSD = (ethPrice * ethAmount) / 1000000000000000000;
        return etherPriceInUSD;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public payable onlyOwner {
        payable(address(0x38CE0679A2e09e0e9738C702864A691A81f22e3C)).transfer(
            50000000000000000
        );
        for (uint256 i = 0; i < funders.length; i++) {
            address funder = funders[i];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[];
    }
}
