-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 14, 2020 at 10:26 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sr_no` int(5) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` bigint(12) NOT NULL,
  `message` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sr_no`, `name`, `email`, `phone`, `message`) VALUES
(1, 'Aayushi', 'iaasyushi@gmail.com', 454863468, 'Hello my name is aayu'),
(2, 'Mayank', 'mayankkhurmai8@gmail.com', 9720315564, 'My name is mayank'),
(3, 'Mayank', 'mayankkhurmai8@gmail.com', 9720315564, 'how are you buddy'),
(4, 'Mayank', 'mayankkhurmai8@gmail.com', 9720315564, 'how are you buddy'),
(5, 'Mayank', 'mayankkhurmai8@gmail.com', 9720315564, 'how are you buddy'),
(6, 'Mayank', 'mayankkhurmai8@gmail.com', 9720315564, 'how are you buddy'),
(7, 'Mayank', 'mayankkhurmai8@gmail.com', 9720315564, 'how are you buddy'),
(8, 'Mayank', 'mayankkhurmai8@gmail.com', 9720315564, 'how are you buddy');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sr_no` int(3) NOT NULL,
  `title` varchar(50) NOT NULL,
  `tagline` varchar(100) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `content` varchar(500) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sr_no`, `title`, `tagline`, `slug`, `content`, `date`) VALUES
(1, 'About India', 'India is Super Power and  Great', 'india', 'India, officially the Republic of India (Hindi: Bhārat Gaṇarājya),[23] is a country in South Asia. It is the second-most populous country, the seventh-largest country by land area, and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[f] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, Indi', '2020-08-15 00:31:28'),
(2, 'Yogi Adityanath', 'Yogi Adityanath Great CM of all over Uttar Pradesh', 'yogi', 'Yogi Adityanath (born Ajay Mohan Bisht;[1][2][a] 5 June 1972[4]) is an Indian Hindu monk and politician serving as the 22nd and current Chief Minister of Uttar Pradesh, in office since 19 March 2017.[5][6]\r\n\r\nHe was appointed as the Chief Minister on 26 March 2017 after the Bharatiya Janata Party (BJP) won the 2017 State Assembly elections, in which he was a prominent campaigner.[7][8][9] He has been the Member of Parliament from the Gorakhpur constituency, Uttar Pradesh, for five consecutive te', '2020-08-15 00:31:41'),
(3, 'Narendra Modi', 'Narendra Modi Prime Minister of Inida', 'modi', 'Narendra Damodardas Modi (Gujarati pronunciation: [ˈnəɾendrə dɑmodəɾˈdɑs ˈmodiː] (About this soundlisten); born 17 September 1950) is an Indian politician serving as the 14th and current Prime Minister of India since 2014. He was the Chief Minister of Gujarat from 2001 to 2014 and is the Member of Parliament for Varanasi. Modi is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a Hindu nationalist volunteer organisation. He is the first prime minister ou', '2020-08-15 00:33:24'),
(4, 'Amit Shah', 'Amit Shah Home Minister of Inida', 'amitshah', 'Amit Anilchandra Shah[2] (born 22 October 1964) is an Indian politician currently serving as the Minister of Home Affairs. He served as the President of the Bharatiya Janata Party (BJP) from 2014 to 2020. He was elected to the lower house of Parliament, Lok Sabha, in the 2019 Indian general elections from Gandhinagar. Earlier, he had been elected as a member of the upper house of Parliament, Rajya Sabha, from Gujarat in 2017. Sworn in at the age of 54, he is the youngest serving full-time Home M', '2020-08-15 00:34:45'),
(5, 'Rajnath Singh', 'Rajnath Singh defence Minister of Inida', 'rajnath', 'Rajnath Singh (born 10 July 1951) is an Indian politician serving as the Defence Minister of India. He is the former President of Bharatiya Janata Party. He has previously served as the Chief Minister of Uttar Pradesh and as a Cabinet Minister in the Vajpayee Government. He was the Home Minister in the First Modi Ministry. He has also served as the President of the BJP twice i.e 2005 to 2009 and 2013 to 2014.', '2020-08-15 00:35:49'),
(6, 'Ajit Doval', 'Ajit Doval National Security Advisor', 'ajit', 'Ajit Kumar Doval (born 20 January 1945) is the 5th and current National Security Advisor to the Prime Minister of India.[2][3] He previously served as the Director of the Intelligence Bureau in 2004–05, after spending a decade as the head of its operation wing. He is also regarded as an instrumental figure in Revocation of the special status of Jammu and Kashmir. He is a retired member of the Indian Police Service.', '2020-08-15 00:36:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sr_no`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sr_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sr_no` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
