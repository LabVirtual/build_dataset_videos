import { DatasetPage } from './app.po';

describe('dataset App', function() {
  let page: DatasetPage;

  beforeEach(() => {
    page = new DatasetPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
