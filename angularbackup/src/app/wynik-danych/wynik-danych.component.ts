import { Component, OnInit } from '@angular/core';
import {ConnectToBlackJackService} from '../connect-to-black-jack.service';

@Component({
  selector: 'app-wynik-danych',
  templateUrl: './wynik-danych.component.html',
  styleUrls: ['./wynik-danych.component.scss']
})
export class WynikDanychComponent implements OnInit {
  Ekspansyjna: { [index: string]: any } = {};
  ReagujNaBank: { [index: string]: any } = {};
  HiLow: { [index: string]: any } = {};
  Intuicyjna: { [index: string]: any } = {};
  NeverBust: { [index: string]: any } = {};
  Prawdopodobna: { [index: string]: any } = {};
  PrzelamPasse: { [index: string]: any } = {};
  PrzetrzymajPasse: { [index: string]: any } = {};
  Podstawowa: { [index: string]: any } = {};
  ZaleznaOdSzczescia: { [index: string]: any } = {};
  Pasujaca: { [index: string]: any } = {};
  Idealna: { [index: string]: any } = {};
  WynikGracza = 0;

  constructor(private server: ConnectToBlackJackService) { }

  ngOnInit() {
    this.Update(this.server.Set);
  }

  Update(tekst: any) {
    this.WynikGracza = tekst.player_score.winning - tekst.player_score.loosing + 0.5 * tekst.player_score.blackjack;

    this.Ekspansyjna.Add('winning', tekst.bots_score.Ekspansyjna.winning);
    this.Ekspansyjna.Add('draw', tekst.bots_score.Ekspansyjna.draw);
    this.Ekspansyjna.Add('loosing', tekst.bots_score.Ekspansyjna.loosing);
    this.Ekspansyjna.Add('blackjack', tekst.bots_score.Ekspansyjna.blackjack);
    this.Ekspansyjna.Add('money', tekst.bots_score.Ekspansyjna.winning - tekst.bots_score.Ekspansyjna.loosing +
      0.5 * tekst.bots_score.Ekspansyjna.blackjack);

    this.ReagujNaBank.Add('winning', tekst.bots_score.ReagujNaBank.winning);
    this.ReagujNaBank.Add('draw', tekst.bots_score.ReagujNaBank.draw);
    this.ReagujNaBank.Add('loosing', tekst.bots_score.ReagujNaBank.loosing);
    this.ReagujNaBank.Add('blackjack', tekst.bots_score.ReagujNaBank.blackjack);
    this.ReagujNaBank.Add('money', tekst.bots_score.ReagujNaBank.winning - tekst.bots_score.ReagujNaBank.loosing +
      0.5 * tekst.bots_score.ReagujNaBank.blackjack);

    this.HiLow.Add('winning', tekst.bots_score.HiLow.winning);
    this.HiLow.Add('draw', tekst.bots_score.HiLow.draw);
    this.HiLow.Add('loosing', tekst.bots_score.HiLow.loosing);
    this.HiLow.Add('blackjack', tekst.bots_score.HiLow.blackjack);
    this.HiLow.Add('money', tekst.bots_score.HiLow.winning - tekst.bots_score.HiLow.loosing + 0.5 * tekst.bots_score.HiLow.blackjack);

    this.Intuicyjna.Add('winning', tekst.bots_score.Intuicyjna.winning);
    this.Intuicyjna.Add('draw', tekst.bots_score.Intuicyjna.draw);
    this.Intuicyjna.Add('loosing', tekst.bots_score.Intuicyjna.loosing);
    this.Intuicyjna.Add('blackjack', tekst.bots_score.Intuicyjna.blackjack);
    this.Intuicyjna.Add('money', tekst.bots_score.Intuicyjna.winning - tekst.bots_score.Intuicyjna.loosing +
      0.5 * tekst.bots_score.Intuicyjna.blackjack);

    this.NeverBust.Add('winning', tekst.bots_score.NeverBust.winning);
    this.NeverBust.Add('draw', tekst.bots_score.NeverBust.draw);
    this.NeverBust.Add('loosing', tekst.bots_score.NeverBust.loosing);
    this.NeverBust.Add('blackjack', tekst.bots_score.NeverBust.blackjack);
    this.NeverBust.Add('money', tekst.bots_score.NeverBust.winning - tekst.bots_score.NeverBust.loosing +
      0.5 * tekst.bots_score.NeverBust.blackjack);

    this.Prawdopodobna.Add('winning', tekst.bots_score.Prawdopodobna.winning);
    this.Prawdopodobna.Add('draw', tekst.bots_score.Prawdopodobna.draw);
    this.Prawdopodobna.Add('loosing', tekst.bots_score.Prawdopodobna.loosing);
    this.Prawdopodobna.Add('blackjack', tekst.bots_score.Prawdopodobna.blackjack);
    this.Prawdopodobna.Add('money', tekst.bots_score.Prawdopodobna.winning - tekst.bots_score.Prawdopodobna.loosing +
      0.5 * tekst.bots_score.Prawdopodobna.blackjack);

    this.PrzelamPasse.Add('winning', tekst.bots_score.PrzelamPasse.winning);
    this.PrzelamPasse.Add('draw', tekst.bots_score.PrzelamPasse.draw);
    this.PrzelamPasse.Add('loosing', tekst.bots_score.PrzelamPasse.loosing);
    this.PrzelamPasse.Add('blackjack', tekst.bots_score.PrzelamPasse.blackjack);
    this.PrzelamPasse.Add('money', tekst.bots_score.PrzelamPasse.winning - tekst.bots_score.PrzelamPasse.loosing +
      0.5 * tekst.bots_score.PrzelamPasse.blackjack);

    this.PrzetrzymajPasse.Add('winning', tekst.bots_score.PrzetrzymajPasse.winning);
    this.PrzetrzymajPasse.Add('draw', tekst.bots_score.PrzetrzymajPasse.draw);
    this.PrzetrzymajPasse.Add('loosing', tekst.bots_score.PrzetrzymajPasse.loosing);
    this.PrzetrzymajPasse.Add('blackjack', tekst.bots_score.PrzetrzymajPasse.blackjack);
    this.PrzetrzymajPasse.Add('money', tekst.bots_score.PrzetrzymajPasse.winning - tekst.bots_score.PrzetrzymajPasse.loosing +
      0.5 * tekst.bots_score.PrzetrzymajPasse.blackjack);

    this.Podstawowa.Add('winning', tekst.bots_score.Podstawowa.winning);
    this.Podstawowa.Add('draw', tekst.bots_score.Podstawowa.draw);
    this.Podstawowa.Add('loosing', tekst.bots_score.Podstawowa.loosing);
    this.Podstawowa.Add('blackjack', tekst.bots_score.Podstawowa.blackjack);
    this.Podstawowa.Add('money', tekst.bots_score.Podstawowa.winning - tekst.bots_score.Podstawowa.loosing +
      0.5 * tekst.bots_score.Podstawowa.blackjack);

    this.ZaleznaOdSzczescia.Add('winning', tekst.bots_score.ZaleznaOdSzczescia.winning);
    this.ZaleznaOdSzczescia.Add('draw', tekst.bots_score.ZaleznaOdSzczescia.draw);
    this.ZaleznaOdSzczescia.Add('loosing', tekst.bots_score.ZaleznaOdSzczescia.loosing);
    this.ZaleznaOdSzczescia.Add('blackjack', tekst.bots_score.ZaleznaOdSzczescia.blackjack);
    this.ZaleznaOdSzczescia.Add('money', tekst.bots_score.ZaleznaOdSzczescia.winning - tekst.bots_score.ZaleznaOdSzczescia.loosing +
      0.5 * tekst.bots_score.ZaleznaOdSzczescia.blackjack);

    this.Pasujaca.Add('winning', tekst.bots_score.Pasujaca.winning);
    this.Pasujaca.Add('draw', tekst.bots_score.Pasujaca.draw);
    this.Pasujaca.Add('loosing', tekst.bots_score.Pasujaca.loosing);
    this.Pasujaca.Add('blackjack', tekst.bots_score.Pasujaca.blackjack);
    this.Pasujaca.Add('money', tekst.bots_score.Pasujaca.winning - tekst.bots_score.Pasujaca.loosing +
      0.5 * tekst.bots_score.Pasujaca.blackjack);

    this.Idealna.Add('winning', tekst.bots_score.Idealna.winning);
    this.Idealna.Add('draw', tekst.bots_score.Idealna.draw);
    this.Idealna.Add('loosing', tekst.bots_score.Idealna.loosing);
    this.Idealna.Add('blackjack', tekst.bots_score.Idealna.blackjack);
    this.Idealna.Add('money', tekst.bots_score.Idealna.winning - tekst.bots_score.Idealna.loosing +
      0.5 * tekst.bots_score.Idealna.blackjack);
  }
}
