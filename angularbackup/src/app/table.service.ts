import { Injectable } from '@angular/core';
import {Card} from './Card.model';
import {Observable, ReplaySubject, Subject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class TableService {
  Row1 = new ReplaySubject<Card[]>();
  Row2 = new ReplaySubject<Card[]>();
  Row3 = new ReplaySubject<Card[]>();

  constructor() { }

  SetRow1(Row1: Card[]) {
    this.Row1.next(Row1);
  }

  SetRow2(Row2: Card[]) {
    this.Row2.next(Row2);
  }

  SetRow3(Row3: Card[]) {
    this.Row3.next(Row3);
  }

  GetRow1() {
    return this.Row1.asObservable();
  }

  GetRow2() {
    return this.Row2.asObservable();
  }

  GetRow3() {
    return this.Row3.asObservable();
  }
}
