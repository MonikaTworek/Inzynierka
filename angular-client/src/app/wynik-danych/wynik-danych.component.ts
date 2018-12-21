import { Component, OnInit } from '@angular/core';
import {ConnectToBlackJackService} from '../connect-to-black-jack.service';

class ScoreRecord {
  name = '-';
  winning = 0;
  draw = 0;
  loosing = 0;
  blackjack = 0;
  money = 0;
}

@Component({
  selector: 'app-wynik-danych',
  templateUrl: './wynik-danych.component.html',
  styleUrls: ['./wynik-danych.component.scss']
})
export class WynikDanychComponent implements OnInit {
  strategie = [];

  mapScore(name, {winning, draw, loosing, blackjack}): ScoreRecord {
    return {
      name: name,
      winning: winning,
      draw: draw,
      loosing: loosing,
      blackjack: blackjack,
      money: (winning - loosing + 0.5 * blackjack) * 10,
    };
  }

  constructor(private server: ConnectToBlackJackService) { }

  ngOnInit() {
    this.Update(this.server.Set());
  }

  Update(tekst: any) {
    this.strategie = [
      this.mapScore(
      'Ekspansyjna', tekst.bots_score[0].Ekspansyjna
    ),
      this.mapScore(
      'ReagujNaBank', tekst.bots_score[1].ReagujNaBank
    ),
      this.mapScore(
      'HiLow', tekst.bots_score[2].HILow
    ),
      this.mapScore(
      'Intuicyjna', tekst.bots_score[3].Intuicyjna
    ),
      this.mapScore(
      'Krupierska', tekst.bots_score[4].Krupierska
    ),
      this.mapScore(
      'NeverBust', tekst.bots_score[5].NeverBust
    ),
      this.mapScore(
      'Prawdopodobna', tekst.bots_score[6].Prawdopodobna
    ),
      this.mapScore(
      'PrzelamPasse', tekst.bots_score[7].PrzelamPasse
    ),
      this.mapScore(
      'PrzetrzymajPasse', tekst.bots_score[8].PrzetrzymajPasse
    ),
      this.mapScore(
      'Podstawowa', tekst.bots_score[9].Podstawowa
    ),
      this.mapScore(
      'ZaleznaOdSzczescia', tekst.bots_score[10].ZaleznaOdSzczescia
    ),
      this.mapScore(
      'Pasujaca', tekst.bots_score[11].Pasujaca
    ),
  ];
    if (tekst.bots_score[12].Idealna.winning !== 0) {
      this.strategie.push(
        this.mapScore(
          'Idealna', tekst.bots_score[12].Idealna
        )
      );
    }
  }
}
