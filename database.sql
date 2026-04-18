-- phpMyAdmin SQL Dump
-- version 4.9.11
-- https://www.phpmyadmin.net/
--
-- Host: database-5003307652.webspace-host.com
-- Erstellungszeit: 18. Apr 2026 um 14:06
-- Server-Version: 5.7.42-log
-- PHP-Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `DB3517771`
--
CREATE DATABASE IF NOT EXISTS `DB3517771` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `DB3517771`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `anmeldung`
--

CREATE TABLE `anmeldung` (
  `sessionID` int(11) NOT NULL,
  `session` varchar(50) DEFAULT NULL,
  `userID` int(11) DEFAULT '0',
  `ip` varchar(50) DEFAULT NULL,
  `url` varchar(50) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `gruppe`
--

CREATE TABLE `gruppe` (
  `gruppeID` int(11) NOT NULL,
  `userID` int(11) DEFAULT '0',
  `name` varchar(50) DEFAULT NULL,
  `ip` varchar(50) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `visible` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `item`
--

CREATE TABLE `item` (
  `ID` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `kompetenz`
--

CREATE TABLE `kompetenz` (
  `ID` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `normFEfs`
--

CREATE TABLE `normFEfs` (
  `nornFEfsID` int(11) NOT NULL,
  `kompetenzID` int(11) DEFAULT '0',
  `p1` float DEFAULT '0',
  `p2` float DEFAULT '0',
  `p3` float DEFAULT '0',
  `p4` float DEFAULT '0',
  `p5` float DEFAULT '0',
  `mi` float DEFAULT '0',
  `sw` float DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `normFEhs`
--

CREATE TABLE `normFEhs` (
  `nornFEhsID` int(11) NOT NULL,
  `kompetenzID` int(11) DEFAULT '0',
  `p1` float DEFAULT '0',
  `p2` float DEFAULT '0',
  `p3` float DEFAULT '0',
  `p4` float DEFAULT '0',
  `p5` float DEFAULT '0',
  `mi` float DEFAULT '0',
  `sw` float DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `normSEfs`
--

CREATE TABLE `normSEfs` (
  `nornSEfsID` int(11) NOT NULL,
  `kompetenzID` int(11) DEFAULT '0',
  `p1` float DEFAULT '0',
  `p2` float DEFAULT '0',
  `p3` float DEFAULT '0',
  `p4` float DEFAULT '0',
  `p5` float DEFAULT '0',
  `mi` float DEFAULT '0',
  `sw` float DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `normSEhs`
--

CREATE TABLE `normSEhs` (
  `nornSEhsID` int(11) NOT NULL,
  `kompetenzID` int(11) DEFAULT '0',
  `p1` float DEFAULT '0',
  `p2` float DEFAULT '0',
  `p3` float DEFAULT '0',
  `p4` float DEFAULT '0',
  `p5` float DEFAULT '0',
  `mi` float DEFAULT '0',
  `sw` float DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `profil`
--

CREATE TABLE `profil` (
  `profilID` int(11) NOT NULL,
  `userID` int(11) DEFAULT '0',
  `gruppeID` int(11) DEFAULT '0',
  `name` varchar(50) DEFAULT '0',
  `item1` int(11) DEFAULT '0',
  `item2` int(11) DEFAULT '0',
  `item3` int(11) DEFAULT '0',
  `item4` int(11) DEFAULT '0',
  `item5` int(11) DEFAULT '0',
  `item6` int(11) DEFAULT '0',
  `item7` int(11) DEFAULT '0',
  `item8` int(11) DEFAULT '0',
  `item9` int(11) DEFAULT '0',
  `item10` int(11) DEFAULT '0',
  `item11` int(11) DEFAULT '0',
  `item12` int(11) DEFAULT '0',
  `item13` int(11) DEFAULT '0',
  `item14` int(11) DEFAULT '0',
  `item15` int(11) DEFAULT '0',
  `item16` int(11) DEFAULT '0',
  `item17` int(11) DEFAULT '0',
  `item18` int(11) DEFAULT '0',
  `item19` int(11) DEFAULT '0',
  `item20` int(11) DEFAULT '0',
  `item21` int(11) DEFAULT '0',
  `item22` int(11) DEFAULT '0',
  `item23` int(11) DEFAULT '0',
  `item24` int(11) DEFAULT '0',
  `item25` int(11) DEFAULT '0',
  `item26` int(11) DEFAULT '0',
  `item27` int(11) DEFAULT '0',
  `item28` int(11) DEFAULT '0',
  `item29` int(11) DEFAULT '0',
  `item30` int(11) DEFAULT '0',
  `item31` int(11) DEFAULT '0',
  `item32` int(11) DEFAULT '0',
  `item33` int(11) DEFAULT '0',
  `item34` int(11) DEFAULT '0',
  `item35` int(11) DEFAULT '0',
  `item36` int(11) DEFAULT '0',
  `kompetenz1` int(11) DEFAULT '0',
  `kompetenz2` int(11) DEFAULT '0',
  `kompetenz3` int(11) DEFAULT '0',
  `kompetenz4` int(11) DEFAULT '0',
  `kompetenz5` int(11) DEFAULT '0',
  `kompetenz6` int(11) NOT NULL,
  `ip` varchar(50) DEFAULT NULL,
  `url` varchar(50) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `visible` tinyint(1) DEFAULT NULL,
  `feitem1` int(11) NOT NULL,
  `feitem2` int(11) NOT NULL,
  `feitem3` int(11) NOT NULL,
  `feitem4` int(11) NOT NULL,
  `feitem5` int(11) NOT NULL,
  `feitem6` int(11) NOT NULL,
  `feitem7` int(11) NOT NULL,
  `feitem8` int(11) NOT NULL,
  `feitem9` int(11) NOT NULL,
  `feitem10` int(11) NOT NULL,
  `feitem11` int(11) NOT NULL,
  `feitem12` int(11) NOT NULL,
  `feitem13` int(11) NOT NULL,
  `feitem14` int(11) NOT NULL,
  `feitem15` int(11) NOT NULL,
  `feitem16` int(11) NOT NULL,
  `feitem17` int(11) NOT NULL,
  `feitem18` int(11) NOT NULL,
  `feitem19` int(11) NOT NULL,
  `feitem20` int(11) NOT NULL,
  `feitem21` int(11) NOT NULL,
  `feitem22` int(11) NOT NULL,
  `feitem23` int(11) NOT NULL,
  `feitem24` int(11) NOT NULL,
  `feitem25` int(11) NOT NULL,
  `feitem26` int(11) NOT NULL,
  `feitem27` int(11) NOT NULL,
  `feitem28` int(11) NOT NULL,
  `feitem29` int(11) NOT NULL,
  `feitem30` int(11) NOT NULL,
  `feitem31` int(11) NOT NULL,
  `feitem32` int(11) NOT NULL,
  `feitem33` int(11) NOT NULL,
  `feitem34` int(11) NOT NULL,
  `feitem35` int(11) NOT NULL,
  `feitem36` int(11) NOT NULL,
  `fekompetenz1` int(11) NOT NULL,
  `fekompetenz2` int(11) NOT NULL,
  `fekompetenz3` int(11) NOT NULL,
  `fekompetenz4` int(11) NOT NULL,
  `fekompetenz5` int(11) NOT NULL,
  `fekompetenz6` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `user`
--

CREATE TABLE `user` (
  `institution` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `vorname` varchar(50) DEFAULT NULL,
  `strasse` varchar(50) DEFAULT NULL,
  `plz` varchar(50) DEFAULT NULL,
  `ort` varchar(50) DEFAULT NULL,
  `tel` varchar(50) DEFAULT NULL,
  `fax` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `url` varchar(50) DEFAULT NULL,
  `ip` varchar(50) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `visible` tinyint(1) DEFAULT NULL,
  `user` varchar(50) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `anmeldung`
--
ALTER TABLE `anmeldung`
  ADD PRIMARY KEY (`sessionID`),
  ADD KEY `sessionID` (`sessionID`),
  ADD KEY `userID` (`userID`);

--
-- Indizes für die Tabelle `gruppe`
--
ALTER TABLE `gruppe`
  ADD PRIMARY KEY (`gruppeID`),
  ADD KEY `gruppeID` (`gruppeID`),
  ADD KEY `userID` (`userID`);

--
-- Indizes für die Tabelle `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID` (`ID`);

--
-- Indizes für die Tabelle `kompetenz`
--
ALTER TABLE `kompetenz`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID` (`ID`);

--
-- Indizes für die Tabelle `normFEfs`
--
ALTER TABLE `normFEfs`
  ADD PRIMARY KEY (`nornFEfsID`),
  ADD KEY `kompetenzID` (`kompetenzID`),
  ADD KEY `nornFEfsID` (`nornFEfsID`);

--
-- Indizes für die Tabelle `normFEhs`
--
ALTER TABLE `normFEhs`
  ADD PRIMARY KEY (`nornFEhsID`),
  ADD KEY `kompetenzID` (`kompetenzID`),
  ADD KEY `nornFEhsID` (`nornFEhsID`);

--
-- Indizes für die Tabelle `normSEfs`
--
ALTER TABLE `normSEfs`
  ADD PRIMARY KEY (`nornSEfsID`),
  ADD KEY `kompetenzID` (`kompetenzID`),
  ADD KEY `nornSEfsID` (`nornSEfsID`);

--
-- Indizes für die Tabelle `normSEhs`
--
ALTER TABLE `normSEhs`
  ADD PRIMARY KEY (`nornSEhsID`),
  ADD KEY `kompetenzID` (`kompetenzID`),
  ADD KEY `nornSEhsID` (`nornSEhsID`);

--
-- Indizes für die Tabelle `profil`
--
ALTER TABLE `profil`
  ADD PRIMARY KEY (`profilID`),
  ADD KEY `gruppeID` (`gruppeID`),
  ADD KEY `profilID` (`profilID`),
  ADD KEY `userID` (`userID`);

--
-- Indizes für die Tabelle `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `anmeldung`
--
ALTER TABLE `anmeldung`
  MODIFY `sessionID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `gruppe`
--
ALTER TABLE `gruppe`
  MODIFY `gruppeID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `item`
--
ALTER TABLE `item`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `kompetenz`
--
ALTER TABLE `kompetenz`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `normFEfs`
--
ALTER TABLE `normFEfs`
  MODIFY `nornFEfsID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `normFEhs`
--
ALTER TABLE `normFEhs`
  MODIFY `nornFEhsID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `normSEfs`
--
ALTER TABLE `normSEfs`
  MODIFY `nornSEfsID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `normSEhs`
--
ALTER TABLE `normSEhs`
  MODIFY `nornSEhsID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `profil`
--
ALTER TABLE `profil`
  MODIFY `profilID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `user`
--
ALTER TABLE `user`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
