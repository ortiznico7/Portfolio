-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2025 at 12:58 AM
-- Server version: 8.0.42
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clientrecords`
--

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

CREATE TABLE `clients` (
  `Name` varchar(50) DEFAULT NULL,
  `ClientID` int NOT NULL,
  `Age` int DEFAULT NULL,
  `CityState` varchar(50) DEFAULT NULL,
  `MonthlyIncome` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `clients`
--

INSERT INTO `clients` (`Name`, `ClientID`, `Age`, `CityState`, `MonthlyIncome`) VALUES
('Nico Ortiz', 1, 17, 'Stamford, CT', '$10,000'),
('Disha Kandasami', 2, 18, 'Stamford, CT', '$15,000'),
('Kei Aguirre', 3, 18, 'Stamford, CT', '$25,000'),
('Carmen Martinez', 4, 56, 'Stamford, CT', '$30,000'),
('Eduardo Ortiz', 5, 58, 'Stamford, CT', '$30,000');

-- --------------------------------------------------------

--
-- Table structure for table `rentdetails`
--

CREATE TABLE `rentdetails` (
  `Name` varchar(50) DEFAULT NULL,
  `ClientID` varchar(50) DEFAULT NULL,
  `DayOfPay` varchar(50) DEFAULT NULL,
  `MonthlyDueDate` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `rentdetails`
--

INSERT INTO `rentdetails` (`Name`, `ClientID`, `DayOfPay`, `MonthlyDueDate`) VALUES
('Nico Ortiz', '1', 'Friday', 'Second of each month'),
('Kei Aguirre', '2', 'Friday', 'First of each month'),
('Disha Kandasami', '3', 'Wednesday', 'First of each month'),
('Carmen Martinez', '4', 'Monday', 'Fifteenth of each month'),
('Eduardo Ortiz', '5', 'Friday', 'Last day of each month');

-- --------------------------------------------------------

--
-- Table structure for table `rentprogress`
--

CREATE TABLE `rentprogress` (
  `ClientID` varchar(50) DEFAULT NULL,
  `IncomeCityState` varchar(50) DEFAULT NULL,
  `MonthlyRent` varchar(50) DEFAULT NULL,
  `OnTime` varchar(3) DEFAULT NULL,
  `LatePay` varchar(3) DEFAULT NULL,
  `AmountOfLatePays` int DEFAULT NULL,
  `RemainingBalance` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `rentprogress`
--

INSERT INTO `rentprogress` (`ClientID`, `IncomeCityState`, `MonthlyRent`, `OnTime`, `LatePay`, `AmountOfLatePays`, `RemainingBalance`) VALUES
('1', 'Darien, CT', '$1,200', 'YES', 'NO', 0, '$30,000'),
('2', 'Middletown, CT', '$1,400', 'YES', 'NO', 0, '$50,000'),
('4', 'Stamford, CT', '$1,300', 'YES', 'NO', 0, '$21,000'),
('5', 'Orangeburg, NY', '$1,200', 'NO', 'YES', 2, '$1,200');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`ClientID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
