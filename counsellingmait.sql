-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 18, 2023 at 11:44 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `counsellingmait`
--

-- --------------------------------------------------------

--
-- Table structure for table `allowed_ip_addresses`
--

CREATE TABLE `allowed_ip_addresses` (
  `id` bigint(20) NOT NULL,
  `ip_address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `allowed_ip_addresses`
--

INSERT INTO `allowed_ip_addresses` (`id`, `ip_address`) VALUES
(1, '127.0.0.1'),
(2, '103.172.73.175');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add login', 1, 'add_login'),
(2, 'Can change login', 1, 'change_login'),
(3, 'Can delete login', 1, 'delete_login'),
(4, 'Can view login', 1, 'view_login'),
(5, 'Can add allowed ip', 2, 'add_allowedip'),
(6, 'Can change allowed ip', 2, 'change_allowedip'),
(7, 'Can delete allowed ip', 2, 'delete_allowedip'),
(8, 'Can view allowed ip', 2, 'view_allowedip'),
(9, 'Can add btech temp', 3, 'add_btechtemp'),
(10, 'Can change btech temp', 3, 'change_btechtemp'),
(11, 'Can delete btech temp', 3, 'delete_btechtemp'),
(12, 'Can view btech temp', 3, 'view_btechtemp'),
(13, 'Can add btech', 4, 'add_btech'),
(14, 'Can change btech', 4, 'change_btech'),
(15, 'Can delete btech', 4, 'delete_btech'),
(16, 'Can view btech', 4, 'view_btech'),
(17, 'Can add btech le temp', 5, 'add_btechletemp'),
(18, 'Can change btech le temp', 5, 'change_btechletemp'),
(19, 'Can delete btech le temp', 5, 'delete_btechletemp'),
(20, 'Can view btech le temp', 5, 'view_btechletemp'),
(21, 'Can add btech le', 6, 'add_btechle'),
(22, 'Can change btech le', 6, 'change_btechle'),
(23, 'Can delete btech le', 6, 'delete_btechle'),
(24, 'Can view btech le', 6, 'view_btechle'),
(25, 'Can add bba temp', 7, 'add_bbatemp'),
(26, 'Can change bba temp', 7, 'change_bbatemp'),
(27, 'Can delete bba temp', 7, 'delete_bbatemp'),
(28, 'Can view bba temp', 7, 'view_bbatemp'),
(29, 'Can add bba', 8, 'add_bba'),
(30, 'Can change bba', 8, 'change_bba'),
(31, 'Can delete bba', 8, 'delete_bba'),
(32, 'Can view bba', 8, 'view_bba'),
(33, 'Can add mba temp', 9, 'add_mbatemp'),
(34, 'Can change mba temp', 9, 'change_mbatemp'),
(35, 'Can delete mba temp', 9, 'delete_mbatemp'),
(36, 'Can view mba temp', 9, 'view_mbatemp'),
(37, 'Can add mba', 10, 'add_mba'),
(38, 'Can change mba', 10, 'change_mba'),
(39, 'Can delete mba', 10, 'delete_mba'),
(40, 'Can view mba', 10, 'view_mba'),
(41, 'Can add log entry', 11, 'add_logentry'),
(42, 'Can change log entry', 11, 'change_logentry'),
(43, 'Can delete log entry', 11, 'delete_logentry'),
(44, 'Can view log entry', 11, 'view_logentry'),
(45, 'Can add permission', 12, 'add_permission'),
(46, 'Can change permission', 12, 'change_permission'),
(47, 'Can delete permission', 12, 'delete_permission'),
(48, 'Can view permission', 12, 'view_permission'),
(49, 'Can add group', 13, 'add_group'),
(50, 'Can change group', 13, 'change_group'),
(51, 'Can delete group', 13, 'delete_group'),
(52, 'Can view group', 13, 'view_group'),
(53, 'Can add user', 14, 'add_user'),
(54, 'Can change user', 14, 'change_user'),
(55, 'Can delete user', 14, 'delete_user'),
(56, 'Can view user', 14, 'view_user'),
(57, 'Can add content type', 15, 'add_contenttype'),
(58, 'Can change content type', 15, 'change_contenttype'),
(59, 'Can delete content type', 15, 'delete_contenttype'),
(60, 'Can view content type', 15, 'view_contenttype'),
(61, 'Can add session', 16, 'add_session'),
(62, 'Can change session', 16, 'change_session'),
(63, 'Can delete session', 16, 'delete_session'),
(64, 'Can view session', 16, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$lHuj3R18PiqN3oFA1ptWQz$RVYwt4rjYLACt5GAmU3OaD4IQ1UNqutHxINrQX/P7m8=', '2023-08-18 21:34:02.988157', 1, 'chanm', '', '', '', 1, 1, '2023-08-18 21:33:07.614509'),
(2, 'pbkdf2_sha256$390000$RVCDIMHCQgQG1Jjlm5Z3k1$wxZn7QuQt9WVsiNadahbdWgyBT6OSLM5eKA6epq5lms=', NULL, 1, 'sadmin', '', '', '', 1, 1, '2023-08-18 21:33:36.814558');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bba`
--

CREATE TABLE `bba` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(255) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `forwarded_address` varchar(255) NOT NULL,
  `browser_info` varchar(1000) NOT NULL,
  `created_at` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bba_temp`
--

CREATE TABLE `bba_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(100) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `forwarded_address` varchar(255) NOT NULL,
  `browser_info` varchar(1000) NOT NULL,
  `created_at` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `btech`
--

CREATE TABLE `btech` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `maths_12th` int(10) UNSIGNED NOT NULL CHECK (`maths_12th` >= 0),
  `physics_12th` int(10) UNSIGNED NOT NULL CHECK (`physics_12th` >= 0),
  `chemistry_12th` int(10) UNSIGNED NOT NULL CHECK (`chemistry_12th` >= 0),
  `english_12th` int(10) UNSIGNED NOT NULL CHECK (`english_12th` >= 0),
  `other_subject_12th` varchar(100) NOT NULL,
  `other_subject_2_12th` varchar(100) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `jee_rank` int(10) UNSIGNED NOT NULL CHECK (`jee_rank` >= 0),
  `jee_percentile` decimal(15,11) NOT NULL,
  `jee_rollno` varchar(100) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `preference1` varchar(125) NOT NULL,
  `preference2` varchar(125) NOT NULL,
  `preference3` varchar(125) NOT NULL,
  `preference4` varchar(125) NOT NULL,
  `preference5` varchar(125) NOT NULL,
  `preference6` varchar(125) NOT NULL,
  `preference7` varchar(125) NOT NULL,
  `preference8` varchar(125) NOT NULL,
  `preference9` varchar(125) NOT NULL,
  `preference10` varchar(125) NOT NULL,
  `preference11` varchar(125) NOT NULL,
  `preference12` varchar(125) NOT NULL,
  `preference13` varchar(125) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `jee_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `forwarded_address` varchar(255) NOT NULL,
  `browser_info` varchar(1000) NOT NULL,
  `created_at` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `btechle`
--

CREATE TABLE `btechle` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(255) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(75) NOT NULL,
  `year_of_12th` varchar(75) NOT NULL,
  `rollno_12th` varchar(75) NOT NULL,
  `school_12th` varchar(125) NOT NULL,
  `aggregate_12th` varchar(75) NOT NULL,
  `maths_12th` varchar(75) NOT NULL,
  `physics_12th` varchar(75) NOT NULL,
  `chemistry_12th` varchar(75) NOT NULL,
  `english_12th` varchar(75) NOT NULL,
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `diploma_bsc_type` varchar(75) DEFAULT NULL,
  `board_diploma_bsc` varchar(75) DEFAULT NULL,
  `year_of_diploma_bsc` varchar(75) DEFAULT NULL,
  `rollno_diploma_bsc` varchar(75) DEFAULT NULL,
  `school_diploma_bsc` varchar(125) DEFAULT NULL,
  `aggregate_diploma_bsc` varchar(75) DEFAULT NULL,
  `ug_degree` varchar(100) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(20) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `preference1` varchar(100) NOT NULL,
  `preference2` varchar(100) NOT NULL,
  `preference3` varchar(100) NOT NULL,
  `preference4` varchar(100) NOT NULL,
  `preference5` varchar(100) NOT NULL,
  `preference6` varchar(100) NOT NULL,
  `preference7` varchar(100) NOT NULL,
  `preference8` varchar(100) NOT NULL,
  `preference9` varchar(100) NOT NULL,
  `preference10` varchar(100) NOT NULL,
  `preference11` varchar(100) NOT NULL,
  `preference12` varchar(100) NOT NULL,
  `preference13` varchar(100) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `diploma_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `forwarded_address` varchar(255) NOT NULL,
  `browser_info` varchar(1000) NOT NULL,
  `created_at` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `btech_le_temp`
--

CREATE TABLE `btech_le_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(75) NOT NULL,
  `year_of_12th` varchar(75) NOT NULL,
  `rollno_12th` varchar(75) NOT NULL,
  `school_12th` varchar(125) NOT NULL,
  `aggregate_12th` varchar(75) NOT NULL,
  `maths_12th` varchar(75) NOT NULL,
  `physics_12th` varchar(75) NOT NULL,
  `chemistry_12th` varchar(75) NOT NULL,
  `english_12th` varchar(75) NOT NULL,
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(100) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `diploma_bsc_type` varchar(75) DEFAULT NULL,
  `board_diploma_bsc` varchar(75) DEFAULT NULL,
  `year_of_diploma_bsc` varchar(75) DEFAULT NULL,
  `rollno_diploma_bsc` varchar(75) DEFAULT NULL,
  `school_diploma_bsc` varchar(125) DEFAULT NULL,
  `aggregate_diploma_bsc` varchar(75) DEFAULT NULL,
  `ug_degree` varchar(100) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(20) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `preference1` varchar(100) NOT NULL,
  `preference2` varchar(100) NOT NULL,
  `preference3` varchar(100) NOT NULL,
  `preference4` varchar(100) NOT NULL,
  `preference5` varchar(100) NOT NULL,
  `preference6` varchar(100) NOT NULL,
  `preference7` varchar(100) NOT NULL,
  `preference8` varchar(100) NOT NULL,
  `preference9` varchar(100) NOT NULL,
  `preference10` varchar(100) NOT NULL,
  `preference11` varchar(100) NOT NULL,
  `preference12` varchar(100) NOT NULL,
  `preference13` varchar(100) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `diploma_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `forwarded_address` varchar(255) NOT NULL,
  `browser_info` varchar(1000) NOT NULL,
  `created_at` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `btech_temp`
--

CREATE TABLE `btech_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `maths_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_12th` >= 0),
  `physics_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`physics_12th` >= 0),
  `chemistry_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`chemistry_12th` >= 0),
  `english_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_12th` >= 0),
  `other_subject_12th` varchar(100) NOT NULL,
  `other_subject_2_12th` varchar(100) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `jee_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`jee_rank` >= 0),
  `jee_percentile` decimal(15,11) DEFAULT NULL,
  `jee_rollno` varchar(100) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `preference1` varchar(125) NOT NULL,
  `preference2` varchar(125) NOT NULL,
  `preference3` varchar(125) NOT NULL,
  `preference4` varchar(125) NOT NULL,
  `preference5` varchar(125) NOT NULL,
  `preference6` varchar(125) NOT NULL,
  `preference7` varchar(125) NOT NULL,
  `preference8` varchar(125) NOT NULL,
  `preference9` varchar(125) NOT NULL,
  `preference10` varchar(125) NOT NULL,
  `preference11` varchar(125) NOT NULL,
  `preference12` varchar(125) NOT NULL,
  `preference13` varchar(125) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `jee_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `forwarded_address` varchar(255) NOT NULL,
  `browser_info` varchar(1000) NOT NULL,
  `created_at` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-08-18 21:35:14.558311', '1', '127.0.0.1', 1, '[{\"added\": {}}]', 2, 1),
(2, '2023-08-18 21:39:51.032041', '2', '103.172.73.125', 1, '[{\"added\": {}}]', 2, 1),
(3, '2023-08-18 21:43:21.988116', '2', '103.172.73.175', 2, '[{\"changed\": {\"fields\": [\"Ip address\"]}}]', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(11, 'admin', 'logentry'),
(13, 'auth', 'group'),
(12, 'auth', 'permission'),
(14, 'auth', 'user'),
(15, 'contenttypes', 'contenttype'),
(2, 'form', 'allowedip'),
(8, 'form', 'bba'),
(7, 'form', 'bbatemp'),
(4, 'form', 'btech'),
(6, 'form', 'btechle'),
(5, 'form', 'btechletemp'),
(3, 'form', 'btechtemp'),
(1, 'form', 'login'),
(10, 'form', 'mba'),
(9, 'form', 'mbatemp'),
(16, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-08-17 16:27:58.881260'),
(2, 'auth', '0001_initial', '2023-08-17 16:27:59.759298'),
(3, 'admin', '0001_initial', '2023-08-17 16:27:59.959764'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-08-17 16:27:59.963871'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-08-17 16:27:59.982313'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-08-17 16:28:00.056872'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-08-17 16:28:00.146103'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-08-17 16:28:00.167459'),
(9, 'auth', '0004_alter_user_username_opts', '2023-08-17 16:28:00.178420'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-08-17 16:28:00.247440'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-08-17 16:28:00.254433'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-08-17 16:28:00.263436'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-08-17 16:28:00.283443'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-08-17 16:28:00.304482'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-08-17 16:28:00.325221'),
(16, 'auth', '0011_update_proxy_permissions', '2023-08-17 16:28:00.334646'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-08-17 16:28:00.354238'),
(18, 'form', '0001_initial', '2023-08-17 16:28:00.664579'),
(19, 'sessions', '0001_initial', '2023-08-17 16:28:00.714265'),
(20, 'form', '0002_alter_bba_first_subject_12th_and_more', '2023-08-17 16:33:49.567372'),
(21, 'form', '0003_alter_mba_rollno_ug_alter_mba_year_of_ug_and_more', '2023-08-17 17:44:24.181840');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('u0gv8phh69ti5utc7jpd7l9ymtr9xxp4', '.eJxVjEEOgjAQRe_StWlKGTvUpXvOQGY6g6CmTSisjHdXEha6_e-9_zIDbes0bFWXYRZzMY05_W5M6aF5B3KnfCs2lbwuM9tdsQetti-iz-vh_h1MVKdvHQIjNdQgnJ3n0EWCRIogGEZpOydOE7YQoRuB1QXkqI59G9ALM6B5fwDXBjem:1qX76Y:lgisjTY_CFrc9Fij2HoWV_qSOprDSWmbL2BjI18SiNc', '2023-09-01 21:34:02.996122');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `password` varchar(25) NOT NULL,
  `candidate_name` varchar(100) NOT NULL,
  `candidate_email` varchar(100) NOT NULL,
  `candidate_mobile` bigint(20) UNSIGNED NOT NULL CHECK (`candidate_mobile` >= 0),
  `course` varchar(100) NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mba`
--

CREATE TABLE `mba` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `other_subject_12th` varchar(100) NOT NULL,
  `other_subject_2_12th` varchar(100) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cat_or_cmat` varchar(10) NOT NULL,
  `cat_or_cmat_rank` int(10) UNSIGNED DEFAULT NULL,
  `cat_or_cmat_rollno` bigint(20) UNSIGNED DEFAULT NULL,
  `ug_type` varchar(75) NOT NULL,
  `board_ug` varchar(75) NOT NULL,
  `year_of_ug` int(10) UNSIGNED DEFAULT NULL,
  `rollno_ug` bigint(20) UNSIGNED DEFAULT NULL,
  `school_ug` varchar(125) NOT NULL,
  `aggregate_ug` varchar(25) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cat_or_cmat_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `ug_degree` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `forwarded_address` varchar(255) NOT NULL,
  `browser_info` varchar(1000) NOT NULL,
  `created_at` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mba_temp`
--

CREATE TABLE `mba_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL,
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cat_or_cmat` varchar(10) NOT NULL,
  `cat_or_cmat_rank` int(10) UNSIGNED DEFAULT NULL,
  `cat_or_cmat_rollno` bigint(20) UNSIGNED DEFAULT NULL,
  `ug_type` varchar(75) NOT NULL,
  `board_ug` varchar(75) NOT NULL,
  `year_of_ug` int(10) UNSIGNED DEFAULT NULL,
  `rollno_ug` bigint(20) UNSIGNED DEFAULT NULL,
  `school_ug` varchar(125) NOT NULL,
  `aggregate_ug` varchar(25) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cat_or_cmat_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `ug_degree` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `forwarded_address` varchar(255) NOT NULL,
  `browser_info` varchar(1000) NOT NULL,
  `created_at` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `allowed_ip_addresses`
--
ALTER TABLE `allowed_ip_addresses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `bba`
--
ALTER TABLE `bba`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bba_temp`
--
ALTER TABLE `bba_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `btech`
--
ALTER TABLE `btech`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `btechle`
--
ALTER TABLE `btechle`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `btech_le_temp`
--
ALTER TABLE `btech_le_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `btech_temp`
--
ALTER TABLE `btech_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `mba`
--
ALTER TABLE `mba`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `mba_temp`
--
ALTER TABLE `mba_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `allowed_ip_addresses`
--
ALTER TABLE `allowed_ip_addresses`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bba`
--
ALTER TABLE `bba`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bba_temp`
--
ALTER TABLE `bba_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `btech`
--
ALTER TABLE `btech`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `btechle`
--
ALTER TABLE `btechle`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `btech_le_temp`
--
ALTER TABLE `btech_le_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `btech_temp`
--
ALTER TABLE `btech_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `mba`
--
ALTER TABLE `mba`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `mba_temp`
--
ALTER TABLE `mba_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
