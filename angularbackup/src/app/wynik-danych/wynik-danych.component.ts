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
  WynikGracza = 0;

  mapScore(name, {winning, draw, loosing, blackjack}): ScoreRecord {
    console.log(arguments);
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
    // this.WynikGracza = (tekst.player_score.winning - tekst.player_score.loosing + 0.5 * tekst.player_score.blackjack) * 10;
    //
    // this.Ekspansyjna.winning = tekst.bots_score.Ekspansyjna.winning;
    // this.Ekspansyjna.draw = tekst.bots_score.Ekspansyjna.draw;
    // this.Ekspansyjna.loosing = tekst.bots_score.Ekspansyjna.loosing;
    // this.Ekspansyjna.blackjack = tekst.bots_score.Ekspansyjna.blackjack;
    // this.Ekspansyjna.money = (tekst.bots_score.Ekspansyjna.winning - tekst.bots_score.Ekspansyjna.loosing +
    //   0.5 * tekst.bots_score.Ekspansyjna.blackjack) * 10;

    console.log(tekst, tekst.bots_score[0], tekst.bots_score[0].Ekspansyjna);

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
    //   this.mapScore(
    //   'Intuicyjna', tekst.bots_score.Intuicyjna
    // ),
      //   this.mapScore(
      //   'Krupierska', tekst.bots_score.Krupierska
      // ),
    //   this.mapScore(
    //   'NeverBust', tekst.bots_score.NeverBust
    // ),
    //   this.mapScore(
    //   'Prawdopodobna', tekst.bots_score.Prawdopodobna
    // ),
    //   this.mapScore(
    //   'PrzelamPasse', tekst.bots_score.PrzelamPasse
    // ),
    //   this.mapScore(
    //   'PrzetrzymajPasse', tekst.bots_score.PrzetrzymajPasse
    // ),
    //   this.mapScore(
    //   'Podstawowa', tekst.bots_score.Podstawowa
    // ),
    //   this.mapScore(
    //   'ZaleznaOdSzczescia', tekst.bots_score.ZaleznaOdSzczescia
    // ),
    //   this.mapScore(
    //   'Pasujaca', tekst.bots_score.Pasujaca
    // ),
  ];
  console.log(this);
    if (true) {
      // this.strategie.push(
      //   this.mapScore(
      //     'Idealna', tekst.bots_score.Idealna
      //   )
      // );
    }
  }
}
